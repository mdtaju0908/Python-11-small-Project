"""
Taju AI Chat - A simple AI chatbot simulation
"""

import random
from datetime import datetime


class TajuAIChat:
    """Taju AI Chatbot - A simple conversational AI."""

    def __init__(self):
        """Initialize the chatbot."""
        self.name = "Taju AI"
        self.conversation_history = []

        self.greetings = [
            "Hello! How can I help you today?",
            "Hi there! What's on your mind?",
            "Hey! Nice to chat with you!",
            "Greetings! I'm here to help.",
            "Welcome! What can I do for you?"
        ]

        self.farewells = [
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Bye! It was nice chatting with you!",
            "Until next time! Stay awesome!",
            "Farewell! Come back anytime!"
        ]

        self.responses = {
            "how are you": [
                "I'm doing great, thanks for asking!",
                "I'm functioning perfectly! How about you?",
                "All systems operational! What about yourself?"
            ],
            "what is your name": [
                "I'm Taju AI, your friendly chatbot!",
                "My name is Taju AI. Nice to meet you!",
                "You can call me Taju AI!"
            ],
            "what can you do": [
                "I can chat, tell jokes, share fun facts, and more!",
                "I'm here to chat and help you with information!",
                "I can have conversations, tell jokes, and entertain!"
            ],
            "tell me a joke": [
                "Why don't scientists trust atoms? They make up everything!",
                "Why did the programmer quit? He didn't get arrays! 😄",
                "What do you call a fake noodle? An impasta!",
                "Why was 6 afraid of 7? Because 7 8 9!",
                "What's a computer's favorite snack? Microchips!"
            ],
            "tell me a fact": [
                "A day on Venus is longer than its year!",
                "Honey never spoils! Ancient honey is still edible.",
                "Octopuses have three hearts!",
                "The Eiffel Tower can grow 15 cm in summer!",
                "A group of flamingos is called a 'flamboyance'!"
            ],
            "what time is it": [
                f"It's currently {datetime.now().strftime('%H:%M:%S')}",
            ],
            "what day is it": [
                f"Today is {datetime.now().strftime('%A, %B %d, %Y')}",
            ],
            "help": [
                "You can ask me about: jokes, facts, time, date, "
                "or just chat!"
            ],
            "thank": [
                "You're welcome! 😊",
                "Happy to help!",
                "Anytime! That's what I'm here for!"
            ],
            "sorry": [
                "No worries at all!",
                "That's okay! Don't worry about it.",
                "No problem! All good!"
            ]
        }

        self.default_responses = [
            "That's interesting! Tell me more.",
            "I see. What else would you like to talk about?",
            "Hmm, let me think about that...",
            "Fascinating! Can you elaborate?",
            "I'm still learning. Can you rephrase that?"
        ]

    def get_response(self, user_input):
        """Generate a response based on user input."""
        user_input_lower = user_input.lower().strip()

        # Check for greetings
        greet_words = ["hello", "hi", "hey", "greetings", "good morning",
                       "good afternoon", "good evening"]
        for word in greet_words:
            if word in user_input_lower:
                return random.choice(self.greetings)

        # Check for farewells
        bye_words = ["bye", "goodbye", "see you", "farewell", "quit", "exit"]
        for word in bye_words:
            if word in user_input_lower:
                return random.choice(self.farewells)

        # Check for keyword matches
        for keyword, responses in self.responses.items():
            if keyword in user_input_lower:
                return random.choice(responses)

        # Default response
        return random.choice(self.default_responses)

    def chat(self, user_input):
        """Process user input and return response."""
        timestamp = datetime.now().strftime("%H:%M:%S")

        # Store user message
        self.conversation_history.append({
            "role": "user",
            "message": user_input,
            "timestamp": timestamp
        })

        # Generate response
        response = self.get_response(user_input)

        # Store bot response
        self.conversation_history.append({
            "role": "bot",
            "message": response,
            "timestamp": timestamp
        })

        return response

    def get_conversation_history(self):
        """Get the conversation history."""
        if not self.conversation_history:
            return "No conversation history yet."

        result = []
        for entry in self.conversation_history:
            role = "You" if entry["role"] == "user" else self.name
            result.append(f"[{entry['timestamp']}] {role}: {entry['message']}")
        return "\n".join(result)

    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []
        return "Conversation history cleared."


def main():
    """Main function to run the chatbot."""
    bot = TajuAIChat()

    print("=" * 50)
    print(f"       Welcome to {bot.name}")
    print("=" * 50)
    print("Type 'help' for available commands")
    print("Type 'history' to see conversation history")
    print("Type 'clear' to clear history")
    print("Type 'bye' to exit")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Please type something!")
            continue

        if user_input.lower() == "history":
            print("\n📜 Conversation History:")
            print(bot.get_conversation_history())
            continue

        if user_input.lower() == "clear":
            print(bot.clear_history())
            continue

        response = bot.chat(user_input)
        print(f"\n{bot.name}: {response}")

        # Check if user wants to exit
        if any(word in user_input.lower() for word in
               ["bye", "goodbye", "quit", "exit"]):
            break


if __name__ == "__main__":
    main()
