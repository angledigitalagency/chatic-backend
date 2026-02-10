import os
import sys

# Ensure we can import agents
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.deliverer import Deliverer

class FluencyDeliverer:
    """
    Handles email delivery for Fluency Radio using the shared Deliverer.
    """
    def __init__(self):
        self.deliverer = Deliverer(identity="fluency")

    def send_email(self, recipient, subject, body_html, body_text=None):
        """
        Delegates to the main Deliverer.
        """
        return self.deliverer.send_email(recipient, subject, body_html, body_text)

    def send_welcome_email(self, recipient, customer_name="Student"):
        """
        Sends the specific Fluency Radio welcome email.
        Calculates the start date (next Friday).
        """
        from datetime import datetime, timedelta

        # Calculate Next Friday
        today = datetime.now()
        # Friday is weekday 4 (Monday=0, Sunday=6)
        days_ahead = 4 - today.weekday()
        if days_ahead <= 0: # Target day already happened this week
            days_ahead += 7
        
        next_friday = today + timedelta(days=days_ahead)
        start_date_str = next_friday.strftime("%A, %B %d")

        # Calculate Meeting Date (Assumption: First meeting is shortly after start, e.g., Tuesday after?)
        # For MVP, user said "Meeting Date". Let's assume it's the Tuesday AFTER the Friday start.
        # Tuesday is weekday 1.
        days_until_meeting = (1 - next_friday.weekday()) + 7 # Tuesday of the *next* week
        first_meeting = next_friday + timedelta(days=days_until_meeting)
        meeting_date_str = first_meeting.strftime("%A, %B %d at 7:00 PM EST") # Placeholder Time

        subject = "Welcome to Fluency Radio! 📻"
        
        body_html = f"""
        <html>
        <body style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #333; line-height: 1.6;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #eee; border-radius: 8px;">
                <h1 style="color: #2c3e50; text-align: center;">Welcome to Fluency Radio! 🎧</h1>
                <p>Hi {customer_name},</p>
                <p>We are thrilled to have you join us. You're all set to start improving your listening skills with our curated song guides.</p>
                
                <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
                
                <h3>📅 Your Schedule</h3>
                <p><strong>Broadcast Starts:</strong> {start_date_str}</p>
                <p>(That's this coming Friday! We'll send you your first <strong>Fluency Guide</strong>—featuring key verbs and vocabulary from our Song of the Week—along with your first challenges.)</p>
                
                <p><strong>First Weekly Meeting:</strong> {meeting_date_str}</p>
                
                <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
                
                <h3>🚀 get Started Now</h3>
                <p>While you wait for Friday, check out the platform instructions and resources:</p>
                <p style="text-align: center;">
                    <a href="https://fluencyradio.com" style="background-color: #3498db; color: white; padding: 12px 24px; text-decoration: none; border-radius: 4px; font-weight: bold;">Go to FluencyRadio.com</a>
                </p>
                
                <p style="margin-top: 30px; font-size: 0.9em; color: #7f8c8d; text-align: center;">
                    Happy Listening,<br>
                    The Fluency Radio Team
                </p>
            </div>
        </body>
        </html>
        """
        
        return self.send_email(recipient, subject, body_html)

    def send_weekly_guide(self, recipient, track_info, guide_data):
        """
        Sends the weekly song guide (Song of the Week).
        Wraps the shared Deliverer's method.
        """
        return self.deliverer.send_song_guide(recipient, track_info, guide_data)
