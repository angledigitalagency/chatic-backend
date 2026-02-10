import os
import sys
import stripe
from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime
from dotenv import load_dotenv

# Ensure we can import agents
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from agents.storage import Storage

load_dotenv()

app = Flask(__name__)

# Stripe Params
stripe.api_key = os.getenv("STRIPE_API_KEY")
# Check for STRIPE_ENDPOINT_SECRET (Production/Render) first, then STRIPE_WEBHOOK_SECRET (Local)
endpoint_secret = os.getenv("STRIPE_ENDPOINT_SECRET") or os.getenv("STRIPE_WEBHOOK_SECRET")

@app.route('/')
def home():
    try:
        with open('landing.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Landing page not found", 404

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.get_data()
    sig_header = request.headers.get('Header-Signature') # Stripe usually uses 'Stripe-Signature'
    # But for simplicity or if using a proxy, verify standard Stripe header:
    sig_header = request.headers.get('Stripe-Signature')

    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return jsonify({'error': 'Invalid payload'}), 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify({'error': 'Invalid signature'}), 400
    
    # DEBUG BYPASS REMOVED

    # Handle the event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        handle_checkout_session(session)
    elif event['type'] == 'payment_intent.succeeded':
        intent = event['data']['object']
        handle_payment_intent(intent)

    return jsonify({'status': 'success'}), 200

from agents.deliverer import Deliverer
from agents.activity_manager import ActivityManager

def handle_checkout_session(session):
    """
    Extracts user info from Stripe session and adds to the appropriate Google Sheet (DB).
    Then triggers 'Fast Access' to catch them up to the current week.
    """
    customer_email = session.get('customer_details', {}).get('email')
    customer_name = session.get('customer_details', {}).get('name')
    customer_id = session.get('customer')
    phone = session.get('customer_details', {}).get('phone', "")
    
    # Check Metadata for Source
    metadata = session.get('metadata', {})
    # 'source' can be 'fluency', 'ifeelsochatty', 'chatic' (legacy)
    source = metadata.get('source', 'ifeelsochatty').lower() 
    
    # Normalize source for logic
    product_db = "ifeelsochatty"
    if "fluency" in source:
        product_db = "fluency"
    
    if customer_email:
        print(f"💰 New Payment: {customer_email} (Source: {source})")
        
        start_date = datetime.now().strftime("%Y-%m-%d")

        # 1. ALWAYS add to the specific Product DB
        storage = Storage(product=product_db)
        storage.add_user(
            email=customer_email,
            phone=phone,
            name=customer_name or "New Student",
            start_date=start_date,
            stripe_id=customer_id,
            source=source
        )
        print(f"   - Added to {product_db} DB.")

        # 2. IF Fluency, ALSO add to the Master iFeelSoChatty DB (Mirroring)
        if product_db == "fluency":
            master_storage = Storage(product="ifeelsochatty")
            master_storage.add_user(
                email=customer_email,
                phone=phone,
                name=customer_name or "New Student",
                start_date=start_date,
                stripe_id=customer_id,
                source=f"{source} (mirrored)"
            )
            print(f"   - Mirrored to ifeelsochatty DB.")
        
        # 3. Welcome Logic Routing
        if product_db == "fluency":
            print(f"📻 Triggering Fluency Radio Welcome for {customer_email}...")
        # Note: We do this AFTER updating the sheet to ensure data is safe.
        # Run in a separate thread to avoid blocking the webhook response (and potential timeout/crash)
        is_new_user = True # Assuming all paid users get welcome for now (MVP)
        if is_new_user:
            import threading
            def send_async_email(email, name, src):
                try:
                    if src == 'fluency':
                        print(f"📻 Triggering Fluency Radio Welcome for {email}...")
                        from agents.deliverer import Deliverer
                        fluency_deliverer = Deliverer(identity="fluency")
                        success = fluency_deliverer.send_welcome_email(email, name)
                        if success:
                            print("✅ Fluency Radio Welcome Email Sent!")
                        else:
                            print("❌ Failed to send Fluency Radio Welcome Email.")
                    else:
                        print(f"📧 Triggering Chatic Welcome for {email}...")
                        chatic_deliverer = Deliverer(identity="chatic")
                        success = chatic_deliverer.send_welcome_email(email, name)
                        if success:
                            print("✅ Chatic Welcome Email Sent!")
                        else:
                            print("❌ Failed to send Chatic Welcome Email.") 
                except Exception as e:
                    print(f"❌ Email sending failed: {e}")

            email_thread = threading.Thread(target=send_async_email, args=(customer_email, customer_name or "Student", product_db))
            email_thread.start()
        else:
            print(f"✨ User {customer_email} already exists. No welcome email sent.")

        # 4. Trigger Test Sequence (if applicable)
        if source == 'fluency_test':
            print(f"🧪 Test Source Detected! Launching 'Fast Forward' Email Stream...")
            import threading
            test_thread = threading.Thread(target=run_test_sequence, args=(customer_email, customer_name))
            test_thread.start()


    else:
        print("⚠️ Payment received but no email found.")

def run_test_sequence(email, name):
    """
    Test Mode: Sends Day 1-7 content sequentially, 1 minute apart.
    """
    import time
    from send_daily_interactions import send_content_for_day
    
    print(f"🧪 STARING TEST SEQUENCE for {email}...")
    
    # Day 0 (Welcome) is already sent by main logic.
    # Start Day 1 after 60s
    for day in range(1, 8): # 1 to 7
        print(f"⏳ Waiting 60s before sending Day {day}...")
        time.sleep(60)
        
        # Hardcode Week 1 for test
        print(f"🚀 Sending Day {day} (Test Mode)...")
        send_content_for_day(email, 1, day)
        
    print(f"✅ TEST SEQUENCE COMPLETE for {email}")



def handle_payment_intent(intent):
    """
    Fallback handler for payment_intent.succeeded if checkout.session.completed is unavailable.
    """
    # PaymentIntent objects usually have 'receipt_email' or we look up the customer
    customer_email = intent.get('receipt_email')
    
    # Sometimes email is in metadata if we put it there, or we have to fetch the customer
    if not customer_email and intent.get('customer'):
        try:
            customer = stripe.Customer.retrieve(intent.get('customer'))
            customer_email = customer.get('email')
        except Exception as e:
            print(f"Error fetching customer for intent: {e}")

    # Metadata extraction
    metadata = intent.get('metadata', {})
    
    # 1. Direct Metadata
    source = metadata.get('source', '').lower()

    # 2. If no source, check if this is a Subscription (Invoice)
    if not source and intent.get('invoice'):
        try:
            invoice_id = intent.get('invoice')
            invoice = stripe.Invoice.retrieve(invoice_id)
            if invoice.get('subscription'):
                subscription = stripe.Subscription.retrieve(invoice.get('subscription'))
                sub_metadata = subscription.get('metadata', {})
                source = sub_metadata.get('source', '').lower()
                print(f"   - Found source in Subscription: {source}")
        except Exception as e:
            print(f"   - Error fetching subscription metadata: {e}")

    # Fallback to default
    if not source:
        source = 'ifeelsochatty'
    customer_name = "Valued Customer"
    if intent.get('shipping'):
         customer_name = intent.get('shipping', {}).get('name', customer_name)
    
    # Normalize source
    product_db = "ifeelsochatty"
    if "fluency" in source:
        product_db = "fluency"

    if customer_email:
        print(f"💰 New Payment (Intent): {customer_email} (Source: {source})")
        
        start_date = datetime.now().strftime("%Y-%m-%d")
        
        # 1. ALWAYS add to the specific Product DB
        storage = Storage(product=product_db)
        storage.add_user(
            email=customer_email,
            phone="", 
            name=customer_name,
            start_date=start_date,
            stripe_id=intent.get('customer') or intent.get('id'),
            source=source
        )
        print(f"   - Added to {product_db} DB.")
        
        # 2. IF Fluency, ALSO add to the Master iFeelSoChatty DB (Mirroring)
        if product_db == "fluency":
            master_storage = Storage(product="ifeelsochatty")
            master_storage.add_user(
                email=customer_email,
                phone="", 
                name=customer_name,
                start_date=start_date,
                stripe_id=intent.get('customer') or intent.get('id'),
                source=f"{source} (mirrored)"
            )
            print(f"   - Mirrored to ifeelsochatty DB.")
        
        # Welcome Logic
        if product_db == "fluency":
            trigger_fluency_welcome(customer_email, customer_name)
        else:
            print(f"✨ Registered iFeelSoChatty user: {customer_email}")
    else:
        print("⚠️ Payment Intent succeeded but no email found.")

def trigger_fluency_welcome(email, name):
    print(f"📻 Triggering Fluency Radio Welcome for {email}...")
    try:
        from fluency_radio.fluency_deliverer import FluencyDeliverer
        fluency_deliverer = FluencyDeliverer()
        success = fluency_deliverer.send_welcome_email(email, name)
        if success:
            print("✅ Fluency Radio Welcome Email Sent!")
        else:
            print("❌ Failed to send Fluency Radio Welcome Email.")
    except Exception as e:
        print(f"❌ Error in Fluency Radio logic: {e}")

@app.route('/api/log-practice', methods=['POST'])
def log_practice():
    """
    Receives practice metrics from Mini-Games (Frontend).
    Payload: {
        "email": "user@example.com",
        "activity_type": "flashcards",
        "details": { "song_title": "...", "time": 120, "score": ... }
    }
    """
    try:
        data = request.json
        email = data.get('email')
        activity_type = data.get('activity_type', 'unknown_game')
        details = data.get('details', {})
        
        if not email:
            return jsonify({'status': 'error', 'message': 'Email required'}), 400
            
        # Log to Storage
        storage_client = Storage(product="fluency") # Use Fluency product context
        storage_client.log_activity(email, activity_type, details)
        
        return jsonify({'status': 'success', 'message': 'Activity logged'}), 200
        
    except Exception as e:
        print(f"Error in log_practice: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/test-email', methods=['GET'])
def test_email():
    """
    Diagnostic Endpoint: Sends a test email to the provided ?email= address.
    """
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'Missing email parameter'}), 400
    
    debug_log = []
    
    try:
        import os
        import resend
        
        # 1. Check Env Vars
        resend_key = os.getenv('RESEND_API_KEY')
        debug_log.append(f"RESEND_API_KEY Present? {bool(resend_key)}")
        if resend_key:
            debug_log.append(f"Key Prefix: {resend_key[:5]}...")
        else:
            return jsonify({'status': 'error', 'message': 'RESEND_API_KEY is MISSING from Environment', 'log': debug_log}), 500

        resend.api_key = resend_key
        
        # 2. Try Sending Directly (Bypass Deliverer for Diagnosis)
        debug_log.append(f"Attempting direct send via 'resend' library to {email}...")
        
        params = {
            "from": "Fluency Radio <onboarding@fluencyradio.com>", 
            "to": [email],
            "subject": "Resend Diagnostic Test 🧪",
            "html": "<h1>It Works!</h1><p>Resend is operational.</p>",
        }
        
        response = resend.Emails.send(params)
        debug_log.append(f"Resend Response: {response}")
        
        return jsonify({
            'status': 'success', 
            'message': 'Email sent via Direct Resend Call!',
            'log': debug_log,
            'response': str(response)
        }), 200
            
    except Exception as e:
        debug_log.append(f"EXCEPTION: {str(e)}")
        return jsonify({
            'status': 'error', 
            'message': str(e),
            'type': str(type(e)),
            'log': debug_log
        }), 500


# --- Game Routes ---

@app.route('/games/flashcards')
def serve_flashcards():
    """
    Serves the Flashcards Mini-Game.
    """
    return send_from_directory('minigames', 'flashcards.html')

@app.route('/games/article-game')
def serve_article_game():
    """
    Serves the Article Mini-Game.
    """
    return send_from_directory('minigames', 'article_game.html')

@app.route('/games/boss-fight')
def serve_boss_fight():
    """
    Serves the Boss Fight Mini-Game (Day 6).
    """
    try:
        return send_from_directory('minigames', 'boss_fight.html')
    except Exception as e:
        return "Boss Fight Not Found", 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4242))
    app.run(host='0.0.0.0', port=port)
