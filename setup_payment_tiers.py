import os
import stripe
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set your Stripe API key
stripe.api_key = os.getenv("STRIPE_API_KEY")

if not stripe.api_key:
    print("Error: STRIPE_API_KEY not found in environment variables.")
    exit(1)

def create_price_and_link(product_id, amount_cents, nickname, currency="usd"):
    try:
        # Create Price
        price = stripe.Price.create(
            product=product_id,
            unit_amount=amount_cents,
            currency=currency,
            recurring={"interval": "month"},
            nickname=nickname,
        )
        print(f"  ✅ Created Price: {nickname} (${amount_cents/100}/mo) -> {price.id}")

        # Create Payment Link
        # Note: We need to ensure metadata is passed to the subscription/payment_intent
        # using subscription_data.metadata for subscriptions.
        link = stripe.PaymentLink.create(
            line_items=[{"price": price.id, "quantity": 1}],
            subscription_data={
                "metadata": {
                    "source": "fluency" if "fluency" in nickname.lower() else "ifeelsochatty",
                    "tier": nickname # Helps track which batch they are in
                }
            },
            metadata={
                 "source": "fluency" if "fluency" in nickname.lower() else "ifeelsochatty"
            }
        )
        print(f"  🔗 Payment Link: {link.url}")
        return price, link
    except Exception as e:
        print(f"  ❌ Error creating price/link for {nickname}: {e}")
        return None, None

def main():
    print("=== 🛒 Setting up Chatic & Fluency Radio Pricing Tiers ===\n")

    # 1. Fluency Radio
    print("--- 1. Fluency Radio Setup ---")
    # Check if exists or create
    # For simplicity in this script, we assume we might need to create it 
    # OR we just add prices to the existing one if we knew the ID. 
    # Let's create a new 'Fluency Radio 2026' product to be clean, or search.
    
    fluency_prods = stripe.Product.search(query="name~'Fluency Radio' AND active:'true'", limit=1)
    if fluency_prods['data']:
        fluency_product = fluency_prods['data'][0]
        print(f"Found existing Fluency Radio product: {fluency_product.name} ({fluency_product.id})")
    else:
        fluency_product = stripe.Product.create(
            name="Fluency Radio",
            description="Access to Fluency Radio + 1 Chatty Hangout/mo",
            metadata={"source": "fluency"}
        )
        print(f"Created new Fluency Radio product: {fluency_product.id}")

    # Fluency Tiers
    # First 10: $10
    create_price_and_link(fluency_product.id, 1000, "Fluency Radio - Batch 1 (First 10)")
    # Next 15: $19
    create_price_and_link(fluency_product.id, 1900, "Fluency Radio - Batch 2 (Next 15)")
    # Next 25: $39
    create_price_and_link(fluency_product.id, 3900, "Fluency Radio - Batch 3 (Next 25)")
    # Standard: $79
    create_price_and_link(fluency_product.id, 7900, "Fluency Radio - Standard")


    print("\n")

    # 2. Chatty Hangouts
    print("--- 2. Chatty Hangouts Setup ---")
    chatty_prods = stripe.Product.search(query="name~'Chatty Hangouts' AND active:'true'", limit=1)
    if chatty_prods['data']:
        chatty_product = chatty_prods['data'][0]
        print(f"Found existing Chatty Hangouts product: {chatty_product.name} ({chatty_product.id})")
    else:
        chatty_product = stripe.Product.create(
            name="Chatty Hangouts",
            description="4 Chatty Sessions/mo + Full Fluency Radio Access",
            metadata={"source": "ifeelsochatty"}
        )
        print(f"Created new Chatty Hangouts product: {chatty_product.id}")

    # Chatty Tiers
    # First 20: $49
    create_price_and_link(chatty_product.id, 4900, "Chatty Hangouts - Batch 1 (First 20)")
    # Next 30: $79
    create_price_and_link(chatty_product.id, 7900, "Chatty Hangouts - Batch 2 (Next 30)")
    # Standard: $149
    create_price_and_link(chatty_product.id, 14900, "Chatty Hangouts - Standard")

if __name__ == "__main__":
    main()
