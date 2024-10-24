import time

def chatbot():
    print("ChatBot: Hello! I'm your assistant. How can I help you today?")
    print("You can ask about the date, time, set reminders, or just have a small chat!")
    
    while True:
        user_input = input("You: ").lower()

        # Exit conditions
        if "exit" in user_input or "bye" in user_input:
            print("ChatBot: Goodbye! Have a great day!")
            break

        # Basic questions
        elif "your name" in user_input:
            print("ChatBot: I am a simple chatbot. You can call me ChatBot!")
        
        elif "time" in user_input:
            current_time = time.strftime("%H:%M:%S")
            print(f"ChatBot: The current time is {current_time}.")

        elif "date" in user_input:
            current_date = time.strftime("%Y-%m-%d")
            print(f"ChatBot: Today's date is {current_date}.")
        
        elif "reminder" in user_input:
            reminder = input("ChatBot: What would you like to be reminded of? ")
            print(f"ChatBot: Reminder set: {reminder}. I will remind you later.")
        
        # Simple small talk
        elif "how are you" in user_input:
            print("ChatBot: I'm just a program, but thanks for asking! How about you?")
        
        elif "thank you" in user_input:
            print("ChatBot: You're welcome!")
        
        # Handle unknown input
        else:
            print("ChatBot: Sorry, I didn't understand that. Can you please rephrase?")
    
if __name__ == "__main__":
    chatbot()
