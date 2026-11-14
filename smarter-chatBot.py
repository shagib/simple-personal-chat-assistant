import datetime
import random

def get_time():
    now = datetime.datetime.now()
    return now.strftime("It's currently %I:%M %p on %A, %B %d, %Y.")

# Expanded memory with lists of choices for variety, plus special commands
responses = {
    "hello": [
        "Hello! How can I help you today?", 
        "Hi there! What can I do for you?"
    ],
    "how are you": [
        "I'm just a program, but I'm doing great! How about you?", 
        "I'm functioning optimally, thank you for asking!",
        "Running smoothly and ready to chat!"
    ],
    "what is your name": [
        "I am a smart ChatBoat", 
        "You can call me ChatBoat",
        "You can call me ChatBoat v2.0!"
    ],
    "motivate me": [
        "Believe in yourself! You can achieve anything you set your mind to.", 
        "You are capable of amazing things! Keep going!",
        "Keep pushing forward. Consistency is the key to mastering Python!"
    ],
    "are you a robot": [
        "Yes, I am a chatbot created to assist you.", 
        "I am an AI-powered assistant designed to help you."
    ],
    "sorry": [
        "No worries! How can I assist you further?", 
        "That's okay! What else can I do for you?"
    ],
}

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower().strip()

    # Handle special dynamic commands
    if "time" in userQuestion or "date" in userQuestion:
        return get_time()

    if "creator" in userQuestion or "who made you" in userQuestion:
        return "I was created by a python developer who is leveling up their coding skills!"

    # Check dictionary for a matching response
    for eachKey in responses:
        if eachKey in userQuestion:
            return random.choice(responses[eachKey])

    # smart fallback 
    fallback_responses = [
        "I'm sorry, I don't understand that. Can you rephrase?", 
        "Hmm, I'm not sure about that. Could you ask something else?", 
        "I wish I could help with that, but I don't have an answer right now."
    ]
    return random.choice(fallback_responses)


def start_chatBot():
    name = input("Welcome, Please enter your name: ").strip()
    presentHour = datetime.datetime.now().hour

    if 5 <= presentHour < 11:
        print(f"Good Morning {name}!")
    elif 11 <= presentHour < 16:
        print(f"Good Afternoon {name}!")
    elif 16 <= presentHour < 20:
        print(f"Good Evening {name}!")
    else:
        print(f"Good Night {name}!")

    print("\nWelcome to ChatBoat v1.0")
    print("Type 'exit', 'quit', or 'bye' to end the conversation.\n")

    while True:
        userInput = input(f"{name}: ")

        # Check exit condition before getting response
        if userInput.lower().strip() in ["exit", "quit", "bye"]:
            print("Goodbye! It was nice chatting with you.")
            break

        replay = getResponseOfBot(userInput)
        print("ChatBoat Response: ", replay)
        print("-" * 40)

if __name__ == "__main__":
    start_chatBot()



    

