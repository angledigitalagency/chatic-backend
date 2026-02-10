
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def test_send_email():
    # Use the Chatic credentials from .env since Fluency ones are missing
    user = os.getenv("EMAIL_HOST_USER")
    password = os.getenv("EMAIL_HOST_PASSWORD")
    host = os.getenv("EMAIL_HOST", "smtp.gmail.com")
    port = int(os.getenv("EMAIL_PORT", 587))
    
    recipient = "feelsochatty@gmail.com" # Test with one of the user's emails
    
    print(f"Attempting to send as: {user}")
    print(f"To: {recipient}")
    
    msg = MIMEMultipart()
    msg["Subject"] = "Test Email from Debug Script"
    msg["From"] = f"Fluency Radio Debug <{user}>"
    msg["To"] = recipient
    
    body = "This is a test email to verify credentials and delivery."
    msg.attach(MIMEText(body, "plain"))
    
    try:
        server = smtplib.SMTP(host, port)
        server.set_debuglevel(1) # Enable verbose debug output
        server.starttls()
        server.login(user, password)
        server.sendmail(user, recipient, msg.as_string())
        server.quit()
        print("\n✅ Email sent successfully!")
    except Exception as e:
        print(f"\n❌ Error sending email: {e}")

if __name__ == "__main__":
    test_send_email()
