#OpenAI_Chat_APP
pip install google.generativeai
import google.generativeai as genai
key = "ENTER YOUR KEY"
print(key)
genai.configure(api_key=key)
Model = genai.GenerativeModel("gemini-2.5-flash")
while True:
    user = input("enter what you want to search or type exit to close ")
    if user.lower() == "exit":
        print("bye bye")
        break
    response = Model.generate_content(user)
    print("bot : ", response.text)