#Email Transfer
import smtplib
import ssl
from email.message import EmailMessage
EMAIL = "mdtaju@example.com"
APP_PASSWORD = "Taju@1234"
RECEIVER = "taju@examnple.com"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "HELLO HOW ARE YOU ....."
msg.set_content("HELLO HOW ARE YOU......")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL, APP_PASSWORD)
    server.send_message(msg)