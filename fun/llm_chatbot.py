import openai


openai.api_key = "YOUR_API_KEY"

def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f" Error: {e}"

def chatbot():
    print(" LLM Chatbot (type 'exit' to quit)")
    print("-" * 40)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Bot: Goodbye! ")
            break
        reply = ask_openai(user_input)
        print(f"Bot: {reply}")

if __name__ == "__main__":
    chatbot()
