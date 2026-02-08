import os
import sys
import stripe
from flask import Flask, request, jsonify
from datetime import datetime
from dotenv import load_dotenv

# Ensure we can import agents
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from agents.storage import Storage

load_dotenv()

app = Flask(__name__)

# Stripe Params
stripe.api_key = os.getenv("STRIPE_API_KEY")
endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

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
        print(f"💰 New Payment: {customer_email} (Source: {source} -> DB: {product_db})")
        
        # Initialize Storage with the correct product/DB
        storage = Storage(product=product_db)
        start_date = datetime.now().strftime("%Y-%m-%d")
        
        # 1. Add User to the correct DB
        storage.add_user(
            email=customer_email,
            phone=phone,
            name=customer_name or "New Student",
            start_date=start_date,
            stripe_id=customer_id,
            source=source
        )
        
        # 2. Welcome Logic Routing
        if product_db == "fluency":
            print(f"📻 Triggering Fluency Radio Welcome for {customer_email}...")
            try:
                from fluency_radio.fluency_deliverer import FluencyDeliverer
                # TODO: Ensure FluencyDeliverer knows which DB to read/write from if needed, 
                # though currently it mostly sends email.
                fluency_deliverer = FluencyDeliverer()
                
                # Send the Welcome Email
                success = fluency_deliverer.send_welcome_email(customer_email, customer_name or "Student")
                
                if success:
                    print("✅ Fluency Radio Welcome Email Sent!")
                else:
                    print("❌ Failed to send Fluency Radio Welcome Email.")
                    
            except Exception as e:
                print(f"❌ Error in Fluency Radio logic: {e}")
        else:
            # iFeelSoChatty Logic
            print(f"✨ Registered iFeelSoChatty user: {customer_email}. No immediate welcome flow defined for generic Chatic yet.")

    else:
        print("⚠️ Payment received but no email found.")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4242))
    app.run(port=port)
