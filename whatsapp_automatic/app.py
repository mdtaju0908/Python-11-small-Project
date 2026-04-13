import st as st
import pywhatkit as kit
import time

st.title("💬 WhatsApp Message Sender")

# Inputs
phone_number = st.text_input("Enter Phone Number (+91...)")
message = st.text_area("Enter Message")

# Send button
if st.button("Send Message"):
    if not phone_number or not message:
        st.error("❌ Please fill all fields")
    else:
        try:
            st.info("⏳ Opening WhatsApp Web...")

            # Delay to avoid instant error
            time.sleep(2)

            kit.sendwhatmsg_instantly(
                phone_no=phone_number,
                message=message,
                wait_time=10,
                tab_close=True
            )

            st.success("✅ Message sent successfully!")

        except Exception as e:
            st.error(f"❌ Error: {e}")