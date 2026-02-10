import os
import stripe
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.getenv("STRIPE_API_KEY")

PRICE_ID = "price_1Sybkk8AUJFYucY51icHx8e2" # Fluency Radio (Early Bird), $39/month

def create_payment_link():
    try:
        print(f"Creating Payment Link for {PRICE_ID}...")
        
        # Check if already exists? Payment Links can be reused.
        # But creating new one is harmless for dev.
        link = stripe.PaymentLink.create(
            line_items=[{"price": PRICE_ID, "quantity": 1}],
            metadata={"source": "fluency_test"},
            after_completion={"type": "hosted_confirmation"}
        )
        
        print(f"Payment Link Created: {link.url}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_payment_link()
