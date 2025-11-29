from twilio.rest import Client

ACCOUNT_SID = "YOUR_ACCOUNT_SID"
AUTH_TOKEN  = "YOUR_AUTH_TOKEN"
FROM_PHONE  = "+1234567890"
TO_PHONE    = "+91XXXXXXXXXX"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

text = input("Enter SMS text: ")

message = client.messages.create(
    body=text,
    from_=FROM_PHONE,
    to=TO_PHONE
)

print("Message sent:", message.sid)
