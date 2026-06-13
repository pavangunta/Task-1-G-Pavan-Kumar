responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! How can I help you?",
    "how are you": "I'm doing great, thanks for asking!",
    "what is ai": "AI is the simulation of human intelligence by machines.",
    "what is your name": "I'm a rule-based chatbot made by Pavan.",
    "bye": "Goodbye! See you next time.",
    "thanks": "You're welcome!",
}

print("Chatbot: Hello! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Chatbot:", responses["bye"])
        break

    reply = responses.get(user_input, "Sorry, I didn't understand that.")
    print("Chatbot:", reply)