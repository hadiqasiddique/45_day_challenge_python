from datetime import datetime

def get_date_input(prompt):
    """Prompt the user for a date and validate the format (YYYY-MM-DD)."""
    while True:
        date_str = input(prompt)
        try:
            # Convert the string to a datetime object
            date_object = datetime.strptime(date_str, "%Y-%m-%d")
            return date_object
        except ValueError:
            print("Invalid format! Please enter the date in YYYY-MM-DD format.")

def calculate_days_between(date1, date2):
    """Calculate the absolute difference in days between two dates."""
    delta = date2 - date1
    return abs(delta.days)

def main():
    print("\n Days Between Dates Calculator \n")

    # Step 1: Get the two dates from the user
    date1 = get_date_input("Enter the first date (YYYY-MM-DD): ")
    date2 = get_date_input("Enter the second date (YYYY-MM-DD): ")

    # Step 2: Calculate the difference in days
    days_between = calculate_days_between(date1, date2)

    # Step 3: Display the result
    print(f"\n The number of days between {date1.date()} and {date2.date()} is {days_between} days.\n")

if __name__ == "__main__":
    main()
