import os
import stripe
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.getenv('STRIPE_API_KEY')

def create_launch_links():
    print("Creating Launch Batch Payment Links...\n")
    
    # 1. Fetch Products
    chatty_hangouts_product = None
    fluency_radio_product = None
    
    for prod in stripe.Product.list(active=True, limit=100):
        if "Chatty Hangouts" in prod.name:
            chatty_hangouts_product = prod
        elif "Fluency Radio (Early Bird)" in prod.name:
            fluency_radio_product = prod
            
    if not chatty_hangouts_product:
        print("❌ Could not find Chatty Hangouts product.")
        return

    # 2. Get $49 Price for Chatty
    prices = stripe.Price.list(product=chatty_hangouts_product.id, active=True)
    launch_price_chatic = None
    for p in prices:
        if p.unit_amount == 4900: # $49
            launch_price_chatic = p
            break
            
    if launch_price_chatic:
        print(f"Found $49 Price: {launch_price_chatic.id}")
        link = stripe.PaymentLink.create(
            line_items=[{"price": launch_price_chatic.id, "quantity": 1}],
            metadata={"source": "ifeelsochatty", "tier": "launch_batch_1"}
        )
        print(f"✅ Created Chatty Launch Link: {link.url}")
    else:
        print("❌ Could not find $49 price for Chatty Hangouts.")

    # 3. Get $10 Price for Fluency (Just to confirm/print)
    prices = stripe.Price.list(product=fluency_radio_product.id, active=True)
    launch_price_fluency = None
    for p in prices:
        if p.unit_amount == 1000: # $10
            launch_price_fluency = p
            break
            
    if launch_price_fluency:
        print(f"Found $10 Price: {launch_price_fluency.id}")
        # Check if link exists or create new? I'll look for existing first just in case to be clean, 
        # but creating a new one is harmless for now.
        link = stripe.PaymentLink.create(
            line_items=[{"price": launch_price_fluency.id, "quantity": 1}],
            metadata={"source": "fluency", "tier": "launch_batch_1"}
        )
        print(f"✅ Created/Confirmed Fluency Launch Link: {link.url}")

if __name__ == "__main__":
    create_launch_links()
