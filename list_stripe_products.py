import os
import stripe
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv("STRIPE_API_KEY")

def list_products():
    try:
        print("Fetching Stripe Products...")
        products = stripe.Product.list(limit=5)
        
        for p in products.data:
            print(f"Product: {p.name} (ID: {p.id})")
            
            prices = stripe.Price.list(product=p.id, limit=3)
            for price in prices.data:
                currency = price.currency.upper()
                amount = price.unit_amount / 100 if price.unit_amount else 0
                interval = f"/{price.recurring.interval}" if price.recurring else ""
                print(f"  - Price: {currency} {amount}{interval} (ID: {price.id})")
                
                # Check for existing Payment Links
                links = stripe.PaymentLink.list(limit=1) # Can't filter by price easily?
                # Actually, creating a new link is safer/easier if I have the Price ID.
                
            print("-" * 30)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_products()
