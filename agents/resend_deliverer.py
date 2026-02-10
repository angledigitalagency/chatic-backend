import os
import resend

class ResendDeliverer:
    def __init__(self):
        # API Key comes from Environment Variable
        api_key = os.getenv('RESEND_API_KEY')
        if not api_key:
            print("❌ Error: RESEND_API_KEY is missing!")
        else:
            resend.api_key = api_key

    def send_welcome_email(self, to_email, name):
        """
        Sends the Welcome Email using Resend API.
        """
        try:
            print(f"📧 Sending Welcome Email via Resend to {to_email}...")
            
            # Using standard template content (simplified for now)
            # In a real app, you might render Jinja2 here or just hardcode the welcome message.
            # Let's use a nice HTML body.
            
            html_content = f"""
            <h1>Welcome to Fluency Radio, {name}! 📻</h1>
            <p>You have successfully unlocked the <strong>Weekly Fluency Program</strong>.</p>
            <p>Your first lesson (Day 1) will arrive in about 1 minute.</p>
            <p>Get ready to tune in!</p>
            <br>
            <p>- The Fluency Radio Team</p>
            """

            params = {
                "from": "Fluency Radio <onboarding@fluencyradio.com>", # Use the domain we are verifying
                "to": [to_email],
                "subject": "Welcome to Fluency Radio! 📻",
                "html": html_content,
            }

            email = resend.Emails.send(params)
            print(f"✅ Email Sent! ID: {email.get('id')}")
            return True

        except Exception as e:
            print(f"❌ Resend Error: {e}")
            return False

    def send_daily_content(self, to_email, subject, html_body):
        """
        Sends Daily Content (Day 1-7).
        """
        try:
            print(f"🚀 Sending '{subject}' via Resend to {to_email}...")
            
            params = {
                "from": "Fluency Radio <daily@fluencyradio.com>",
                "to": [to_email],
                "subject": subject,
                "html": html_body,
            }

            email = resend.Emails.send(params)
            print(f"✅ Daily Email Sent! ID: {email.get('id')}")
            return True

        except Exception as e:
            print(f"❌ Resend Error: {e}")
            return False
