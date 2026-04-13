# 📧 Email Sender

A convenient tool built with Streamlit to send emails using Gmail's SMTP service.

## 🛠️ Installation

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Setup

1. Create a `.env` file in the `Email_Sender` directory.
2. Add your Gmail credentials to the `.env` file:
   ```env
   EMAIL=your_email@gmail.com
   APP_PASSWORD=your_app_password
   ```
   *Note: Use a Google App Password, not your regular Gmail password.*

## 🚀 How to Use

1. Run the Streamlit app:
   ```bash
   streamlit run email.py
   ```
2. Enter the **Receiver Email**, **Subject**, and **Message**.
3. Click **Send Email** to send it via Gmail SMTP.
