# rule based chatbot
import datetime
import time

name = input("Welcome, Please enter your name: ")

presentHour = datetime.datetime.now().hour

if 5 <= presentHour < 11:
    print(f"Good Morning {name}!")
elif 11 <= presentHour < 16:
    print(f"Good Afternoon {name}!")
elif 16 <= presentHour < 20:
    print(f"Good Evening {name}!")
else:
    print(f"Good Night {name}!")

print("Welcome to ChatBoat")
print("This is a simple chatbot that can answer your questions. Type 'exit' to end the conversation.")

# Chatboat Memory Creation [ dictionary of responses ] 
responses = {
    "hello": "Hello! How can I help you today?",
    "how are you": "I'm just a program, but I'm doing great! How about you?",
    "what is your name": "I am a smart ChatBoat",
    "motivate me": "Believe in yourself! You can achieve anything you set your mind to.",
    "are you a robot": "Yes, I am a chatbot created to assist you.",
    "sorry": "No worries! How can I assist you further?",
    "exit": "Goodbye! It was nice chatting with you."
}

# function to get response of chatboat
def getResponseOfBoat(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I'm sorry, I don't understand that."     

while True:
    # User Input
    userInput = input("Please ask your question:")
    replay = getResponseOfBoat(userInput)
    print("ChatBoat Response: ", replay)

    if "exit" in userInput.lower():
        break