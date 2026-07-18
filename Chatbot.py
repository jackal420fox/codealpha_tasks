print("=" * 40)
print("      BASIC CHATBOT")
print("=" * 40)
print("Type 'bye' anytime to exit.\n")

while True:

    message = input("You : ").lower()

    if message == "hello":
        print("Bot : Hi!")

    elif message == "hi":
        print("Bot : Hello!")

    elif message == "how are you":
        print("Bot : I'm fine, thanks!")

    elif message == "what is your name":
        print("Bot : I am CodeAlpha Chatbot.")

    elif message == "who created you":
        print("Bot : I was created using Python.")

    elif message == "what can you do":
        print("Bot : I can answer simple predefined questions.")

    elif message == "thank you":
        print("Bot : You're welcome!")

    elif message == "bye":
        print("Bot : Goodbye!")
        break

    else:
        print("Bot : Sorry, I don't understand that.")