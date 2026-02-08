import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
# from twilio.rest import Client  <-- Removed to lazy load

class Deliverer:
    def __init__(self, identity="chatic"):
        self.identity = identity
        self.smtp_server = os.getenv("EMAIL_HOST", "smtp.gmail.com")
        self.smtp_port = os.getenv("EMAIL_PORT", 587)
        
        if identity == "fluency":
            self.username = os.getenv("FLUENCY_EMAIL_USER")
            self.password = os.getenv("FLUENCY_EMAIL_PASSWORD")
            # Fallback to shared credentials if specific ones are missing
            if not self.username:
                print("⚠️ Fluency credentials missing. Falling back to shared email.")
                self.username = os.getenv("EMAIL_HOST_USER")
                self.password = os.getenv("EMAIL_HOST_PASSWORD")
            
            self.display_name = "Fluency Radio"
        else:
            # Default to Chatic
            self.username = os.getenv("EMAIL_HOST_USER")
            self.password = os.getenv("EMAIL_HOST_PASSWORD")
            self.display_name = "I Feel So Chatty"
        
        # Twilio Config (Shared for now, or could be split too)
        self.twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.twilio_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.twilio_phone = os.getenv("TWILIO_PHONE_NUMBER")
        self.twilio_client = None 
        # Lazy load client only when sending SMS to save memory

    def send_email(self, recipient, subject, body_html, body_text=None):
        """
        Sends an email using the configured SMTP server and identity.
        """
        if not all([self.smtp_server, self.smtp_port, self.username, self.password]):
            print(f"Error: SMTP configuration missing for identity '{self.identity}'. Check .env variables.")
            return False

        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            # Format: "Display Name <email@example.com>"
            msg["From"] = f"{self.display_name} <{self.username}>"
            msg["To"] = recipient

            # Attach plain text version (optional fallback)
            if body_text:
                part1 = MIMEText(body_text, "plain")
                msg.attach(part1)

            # Attach HTML version
            part2 = MIMEText(body_html, "html")
            msg.attach(part2)

            # Connect and send
            with smtplib.SMTP(self.smtp_server, int(self.smtp_port)) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.sendmail(self.username, recipient, msg.as_string())
            
            print(f"Email sent successfully to {recipient}")
            return True

        except Exception as e:
            print(f"Failed to send email: {e}")
            return False

    def send_welcome_email(self, recipient, track_info, guide_data):
        """
        Formats and sends the welcome email with Spotify link and Fluency Guide.
        Replaces full lyrics with a copyright-compliant summary.
        """
        if not track_info:
            print("Error: No track info provided.")
            return False

        subject = f"🎵 Song of the Week: {track_info.get('title', 'Unknown Track')}"
        
        # Unpack Guide Data
        target_verbs = guide_data.get('target_verbs', [])
        top_sentences = guide_data.get('top_sentences', [])
        
        # Format Lists for HTML
        verbs_html = "".join([f"<li>{v}</li>" for v in target_verbs[:5]]) # Top 5 verbs
        sentences_html = "".join([f"<li style='margin-bottom: 8px;'><em>\"{s}\"</em></li>" for s in top_sentences[:3]]) # Top 3 sentences

        # HTML Template
        html_content = f"""
        <html>
        <body style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333; line-height: 1.6;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #eee; border-radius: 12px; background-color: #f9f9f9;">
                
                <!-- HEADER -->
                <div style="text-align: center; padding-bottom: 20px; border-bottom: 2px solid #3498db;">
                    <h2 style="color: #2c3e50; margin-bottom: 5px;">{self.display_name} 📻</h2>
                    <p style="color: #7f8c8d; margin-top: 0;">Song of the Week</p>
                </div>

                <!-- SONG INFO -->
                <div style="text-align: center; padding: 20px 0;">
                    <h1 style="font-size: 24px; margin-bottom: 5px;">{track_info.get('title')}</h1>
                    <h3 style="color: #7f8c8d; font-weight: normal; margin-top: 0;">by {track_info.get('artist')}</h3>
                    
                    <a href="{track_info.get('external_url')}" 
                       style="display: inline-block; background-color: #1DB954; color: white; padding: 12px 24px; 
                              text-decoration: none; border-radius: 25px; font-weight: bold; margin-top: 10px;">
                        🎧 Listen on Spotify
                    </a>
                </div>

                <!-- FLUENCY GUIDE -->
                <div style="background-color: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                    <h3 style="color: #e67e22; border-bottom: 1px solid #eee; padding-bottom: 10px;">🧠 Fluency Guide</h3>
                    
                    <p><strong>Target Verbs to Hear:</strong></p>
                    <ul>
                        {verbs_html if verbs_html else "<li>No specific target verbs valid for this song.</li>"}
                    </ul>

                    <p><strong>Key Phrases:</strong></p>
                    <ul>
                        {sentences_html if sentences_html else "<li>Listen closely to the lyrics!</li>"}
                    </ul>
                </div>

                <!-- FOOTER -->
                <div style="text-align: center; margin-top: 30px; font-size: 12px; color: #aaa;">
                    <p>Keep listening. Keep learning.</p>
                    <p><em>Fluency Radio Team</em></p>
                </div>

                </div>
        </body>
        </html>
        """
        
        # Plain Text Fallback
        text_content = f"""
        Fluency Radio - Song of the Week
        
        Track: {track_info.get('title')}
        Artist: {track_info.get('artist')}
        Listen: {track_info.get('external_url')}
        
        --- FLUENCY GUIDE ---
        
        Target Verbs:
        {', '.join(target_verbs[:5])}
        
        Key Phrases:
        {chr(10).join(['- ' + s for s in top_sentences[:3]])}
        
        Happy Listening!
        """

        return self.send_email(recipient, subject, html_content, text_content)

    def send_sms(self, to_number, body):
        """
        Sends an SMS using Twilio.
        """
        if not self.twilio_sid or not self.twilio_token or not self.twilio_phone:
            print("Twilio not configured.")
            return False
            
        try:
            # Lazy load Twilio Client
            from twilio.rest import Client
            if not self.twilio_client:
                self.twilio_client = Client(self.twilio_sid, self.twilio_token)

            message = self.twilio_client.messages.create(
                body=body,
                from_=self.twilio_phone,
                to=to_number
            )
            print(f"SMS sent: {message.sid}")
            return True
        except Exception as e:
            print(f"Failed to send SMS: {e}")
            return False
