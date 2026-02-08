from fluency_radio.fluency_deliverer import FluencyDeliverer
import sys

email = sys.argv[1] if len(sys.argv) > 1 else input("Enter test email: ")
print(f"Sending test Fluency Radio email to {email}...")

d = FluencyDeliverer()
d.send_welcome_email(email, "Test User")
