
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

def verify_fluency_auth():
    print("🕵️‍♂️ Verifying Fluency Radio Credentials...")
    
    # 1. Check for Env Vars OR Use Provided Credentials
    user = os.getenv("FLUENCY_EMAIL_USER") or "fluencyradio@gmail.com"
    # Using the App Password provided by the user
    password = os.getenv("FLUENCY_EMAIL_PASSWORD") or "lydi pucf iizr phxy"
    
    if not user:
        print("❌ 'FLUENCY_EMAIL_USER' is missing from .env")
        # Hardcoding expectation for the user to see
        print("   -> expected: fluencyradio@gmail.com")
        
    if not password:
        print("❌ 'FLUENCY_EMAIL_PASSWORD' is missing from .env")
    
    if not user or not password:
        print("\n⚠️ Cannot attempt login without credentials.")
        print("Please add them to your .env file or Render environment.")
        return

    # 2. Attempt SMTP Login
    print(f"\n🔐 Attempting to login as: {user}")
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, password)
        server.quit()
        print("✅ SUCCESS! Password is valid. access granted.")
    except smtplib.SMTPAuthenticationError:
        print("❌ FAILURE: Username/Password rejected by Google.")
        print("   - Check if the App Password is correct.")
        print("   - Ensure 2-Step Verification is ON.")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

if __name__ == "__main__":
    verify_fluency_auth()
