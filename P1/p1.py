from datetime import datetime
import random

print("\n========== DECODELABS AI CHATBOT ==========\n")

print("Bot: Hello! I am DecodeLabs AI Chatbot.")
print("Type 'help' to see commands.")
print("Type 'exit' anytime to quit.\n")

jokes = [
    "Why did the computer get cold? Because it left its Windows open!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "I would tell you a coding joke, but it might not compile."
]

quotes = [
    "Success starts with consistent effort.",
    "Small progress is still progress.",
    "Practice today, improve tomorrow."
]

while True:

    user = input("You: ").strip().lower()

    # Greetings
    if user in ["hi","hello","hey"]:

        print("Bot: Hello! Nice to meet you.")

    # Bot Name
    elif user in ["your name","who are you"]:

        print("Bot: I am DecodeLabs AI Chatbot.")

    # Status
    elif user == "how are you":

        print("Bot: I'm functioning perfectly!")

    # Date & Time
    elif user == "time":

        print("Bot:", datetime.now().strftime("%I:%M %p"))

    elif user == "date":

        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    # Joke
    elif user == "joke":

        print("Bot:", random.choice(jokes))

    # Motivation
    elif user == "motivate me":

        print("Bot:", random.choice(quotes))

    # Simple Calculator
    elif user == "calculator":

        try:

            num1 = float(input("Enter first number: "))
            op = input("Choose (+ - * /): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                print("Bot: Result =", num1 + num2)

            elif op == "-":
                print("Bot: Result =", num1 - num2)

            elif op == "*":
                print("Bot: Result =", num1 * num2)

            elif op == "/":
                print("Bot: Result =", num1 / num2)

            else:
                print("Bot: Invalid operator.")

        except:
            print("Bot: Invalid calculation input.")

    # Help Menu
    elif user == "help":

        print("""
Available Commands:

hello / hi / hey
how are you
your name
time
date
joke
motivate me
calculator
exit
""")

    # Exit
    elif user in ["bye","quit","exit"]:

        print("Bot: Goodbye! Have a great day.")
        break

    # Unknown Input
    else:

        print("Bot: Sorry, I don't understand that yet.")
