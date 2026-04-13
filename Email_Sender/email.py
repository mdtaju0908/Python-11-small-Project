import st as st
import smtplib
import ssl
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Load .env
load_dotenv()

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

st.title("📧 Email Sender")

# User inputs
receiver_email = st.text_input("Receiver Email")
subject = st.text_input("Subject")
message = st.text_area("Message")

if st.button("Send Email"):
    if not receiver_email or not subject or not message:
        st.error("❌ Please fill all fields")
    else:
        try:
            msg = EmailMessage()
            msg["From"] = EMAIL
            msg["To"] = receiver_email
            msg["Subject"] = subject
            msg.set_content(message)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(EMAIL, APP_PASSWORD)
                server.send_message(msg)

            st.success("✅ Email sent successfully!")

        except Exception as e:
            st.error(f"❌ Error: {e}")