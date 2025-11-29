import pywhatkit as kit

# WhatsApp number with country code
phone_number = "+91XXXXXXXXXX"

message = "Hello from Python automation "

# Instantly send message using WhatsApp Web
kit.sendwhatmsg_instantly(phone_no=phone_number, message=message)

print("Message sent successfully!")
