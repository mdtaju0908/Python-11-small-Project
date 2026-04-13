# 📩 SMS Sender

An automation tool built with Streamlit and Twilio to send SMS messages directly from your browser.

## 🛠️ Installation

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Setup

1. Create a `.env` file in the `SMS_Automation` directory.
2. Add your Twilio credentials to the `.env` file:
   ```env
   ACCOUNT_SID=your_twilio_sid
   AUTH_TOKEN=your_twilio_auth_token
   FROM_PHONE=your_twilio_phone_number
   ```

## 🚀 How to Use

1. Run the Streamlit app:
   ```bash
   streamlit run sms.py
   ```
2. Enter the **Receiver Phone** number (including country code, e.g., +91...).
3. Type your **Message**.
4. Click **Send SMS** to deliver the message via Twilio.
