# Greeting Message Generator

A simple Python program that generates a personalized greeting message based on the current time of day and an optional occasion.

## Features
- Detects the **time of day** (morning, afternoon, evening) automatically.
- Generates personalized greetings for **any name**.
- Allows adding an **occasion** (e.g., Birthday, Anniversary, Eid).
- Handles cases where the occasion is not provided.
- Clean and simple code using Python’s `datetime` module.

## Requirements
- **Python 3.8+**

## How to Run
1. Make sure you have Python installed.  
   You can check your version with:
   ```bash
   python --version
2. Save the code as greeting_message_generator.py.

3. Open a terminal in the same directory.

4. Run the program:
python greeting_message_generator.py

**Example Usage**
- Welcome to Greeting Message Generator!

- Enter your name: Hadiqa

- Enter the occasion: Birthday

- Good morning Hadiqa, wishing you a wonderful Birthday.

**How It Works**

1. Time Detection:

- Uses datetime.now().hour to decide:

Morning: before 12 PM

Afternoon: 12 PM – 6 PM

Evening: after 6 PM

2. Greeting Generation:
Combines time of day with the user's name and optional occasion.


