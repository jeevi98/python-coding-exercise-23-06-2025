def chatbot():
    print(" Rule-Based Chatbot (type 'bye' to exit)")
    print("-" * 40)

    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there!",
        "how are you": "I'm just a bot, but I'm doing well!",
        "what is your name": "I'm RuleBot, your assistant.",
        "bye": "Goodbye! Have a great day!",
        "thanks": "You're welcome!",
        "help": "You can ask me basic questions like 'hi', 'bye', or 'how are you'."
    }

    while True:
        user_input = input("You: ").lower().strip()
        if user_input == 'bye':
            print("Bot: Goodbye! ")
            break
        response = responses.get(user_input, "Sorry, I don't understand that. ")
        print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot()
