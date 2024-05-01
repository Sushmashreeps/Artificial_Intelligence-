def chatbot(user_input):
    # Predefined rules and responses
    rules = {
        "hi": "Hello! How can I assist you?",
        "how are you?": "I'm just a bot, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm sorry, I didn't understand that."
    }

    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if user input matches any predefined rules
    if user_input in rules:
        return rules[user_input]
    else:
        return rules["default"]

# Main function to interact with the chatbot
def main():
    print("Welcome to the simple chatbot!")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = chatbot(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
