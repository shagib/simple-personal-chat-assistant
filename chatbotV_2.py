import datetime
import random
import difflib

class AdvancedChatBot:
    def __init__(self, name="ChatBot v2.0"):
        self.name = name
        self.user_name = ""
        self.chat_history = [] # conversion history

        # keyword and answers
        self.responses = {
            "hello": [
                "Hello! How can I assist your coding journey today?", 
                "Hi there! Ready to write some code?"
            ],
            "how are you": [
                "I'm operating at peak performance! How are you doing?", 
                "All systems nominal and ready for action!"
            ],
            "python": [
                "Python is a high-level, interpreted programming language known for its readability.",
                "Love Python! Are you working on web development, AI, or automation?"
            ],
            "joke": [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "There are 10 types of people in the world: those who understand binary, and those who don't."
            ],
            "exit": [
                "Goodbye! Keep coding and building amazing things.",
                "Catch you later! Have a great coding session."
            ]
        }

    def get_time_date(self):
        now = datetime.datetime.now()
        return now.strftime("Current time is %I:%M %p on %A, %B %d, %Y.")

    def find_best_match(self, user_input):
        keys = list(self.responses.keys())

        matches = difflib.get_close_matches(user_input, keys, n=1, cutoff=0.6)

        if matches:
            return matches[0] 
        return None

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
    
        if "time" in user_input or "date" in user_input:
            return self.get_time_date()

        if "history" in user_input:
            return f"We've had {len(self.chat_history)} exchanges in this session."

        matched_key = self.find_best_match(user_input)

        if matched_key:
            return random.choice(self.responses[matched_key])

        fallback_responses = [
            "That's an interesting question, but I'm still learning!",
            "I couldn't find a match for that. Try asking about Python, time, or a joke.",
            "Could you rephrase that? My knowledge base is expanding daily."
        ]
        return random.choice(fallback_responses)

    def start(self):
        print(f"--- Welcome to {self.name} ---")
        self.user_name = input("Please enter your name: ").strip()

        hour = datetime.datetime.now().hour
        greeting = "Good morning" if 5 <= hour < 12 else "Good afternoon" if 12 <= hour < 18 else "Good evening"
        print(f"{greeting}, {self.user_name}!\nType 'exit' to quit.\n")

        while True:
            user_msg = input(f"{self.user_name}: ")

            if user_msg.lower().strip() in ["exit", "quit", "bye"]:
                farewell = random.choice(self.responses["exit"])
                print(f"{self.name}: {farewell}")
                break

            self.chat_history.append({"user": user_msg})

            bot_response = self.get_response(user_msg)

            self.chat_history.append({"bot": bot_response})

            print(f"{self.name}: {bot_response}")
            print("-" * 50)


if __name__ == "__main__":
    bot = AdvancedChatBot()
    bot.start()            
    
