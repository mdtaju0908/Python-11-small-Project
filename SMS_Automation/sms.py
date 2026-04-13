import st as st
import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load env
load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
FROM_PHONE = os.getenv("FROM_PHONE")

st.title("📩 SMS Sender")

# Inputs
to_phone = st.text_input("Receiver Phone (+91...)")
message_text = st.text_area("Enter Message")

if st.button("Send SMS"):
    if not to_phone or not message_text:
        st.error("❌ Fill all fields")
    else:
        try:
            client = Client(ACCOUNT_SID, AUTH_TOKEN)

            message = client.messages.create(
                body=message_text,
                from_=FROM_PHONE,
                to=to_phone
            )

            st.success(f"✅ Message sent! SID: {message.sid}")

        except Exception as e:
            st.error(f"❌ Error: {e}")