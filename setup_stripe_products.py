
import os
import stripe
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.getenv('STRIPE_API_KEY')

def create_product(name, description, amount, interval, currency="usd", metadata=None):
    print(f"Creating/Updating: {name}...")
    
    # 1. create Product
    try:
        product = stripe.Product.create(
            name=name,
            description=description,
            metadata=metadata or {}
        )
        print(f"  ✅ Product created: {product.id}")
    except Exception as e:
        print(f"  ❌ Product creation failed: {e}")
        return

    # 2. Create Price
    try:
        if interval == "one-time":
            price = stripe.Price.create(
                unit_amount=int(amount * 100),
                currency=currency,
                product=product.id,
            )
        else:
            price = stripe.Price.create(
                unit_amount=int(amount * 100),
                currency=currency,
                recurring={"interval": interval},
                product=product.id,
            )
        print(f"  ✅ Price created: {price.id} (${amount} {interval})")
        
        # 3. Create Payment Link
        link = stripe.PaymentLink.create(
            line_items=[{"price": price.id, "quantity": 1}],
            metadata=metadata or {} # Pass metadata to checkout session
        )
        print(f"  🔗 Payment Link: {link.url}")
        
    except Exception as e:
        print(f"  ❌ Price/Link creation failed: {e}")

if __name__ == "__main__":
    print("=== Setting up Stripe Products ===\n")

    # 1. Fluency Radio (Standard/Anchor)
    create_product(
        name="Fluency Radio (Premium)",
        description="Full access to Fluency Radio song guides + 1 Weekly Group Session.",
        amount=79.00,
        interval="month",
        metadata={"source": "fluency", "tier": "premium"}
    )
    
    print("\n-----------------------------------\n")

    # 2. Fluency Radio (Early Bird - Pilot)
    create_product(
        name="Fluency Radio (Early Bird)",
        description="Limited time offer: Weekly access to Fluency Radio content.",
        amount=9.99,
        interval="week", # User specified "per week"
        metadata={"source": "fluency", "tier": "early-bird"}
    )

    print("\n-----------------------------------\n")

    # 3. Chatty Single Session
    create_product(
        name="Chatty Group Session",
        description="Single drop-in pass for an iFeelSoChatty group session.",
        amount=16.00,
        interval="one-time",
        metadata={"source": "ifeelsochatty", "type": "single-session"}
    )
    
    print("\n-----------------------------------\n")
    
    # 4. iFeelSoChatty Bundle (Mock based on conversation)
    # User mentioned ~ $84 or similar. Let's create a Placeholder if needed, or skip.
    # User said "Chatty session... $16 each, making it $84". 
    # Let's create a "Monthly 4-Pack" bundle as a common request? 
    # 4 * 16 = 64. Plus Fluency ($??). 
    # Let's stick to the explicitly requested ones first.
