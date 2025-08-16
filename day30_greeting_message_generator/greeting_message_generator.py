from datetime import datetime

def get_time_of_day():
    """Determine the current time of day (morning, afternoon, evening)."""
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "morning"
    elif 12 <= current_hour < 18:
        return "afternoon"
    else:
        return "evening"

def generate_greeting(name, occasion=None):
    """Generate a personalized greeting message."""
    time_of_day = get_time_of_day()
    if occasion:
        return f"Good {time_of_day} {name}, wishing you a wonderful {occasion}."
    else:
        return f"Good {time_of_day} {name}, hope you have a good day."

def main():
    print("Welcome to Greeting Message Generator!")
    
    name = input("Enter your name: ").strip()
    occasion = input("Enter the occasion: ").strip()

    if not name:
        print("Please enter your name.")
        return

    greeting = generate_greeting(name, occasion if occasion else None)
    print(greeting)

if __name__ == "__main__":
    main()
