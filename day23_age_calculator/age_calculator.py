from datetime import date, datetime

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year

    # Adjust if birthday hasn't happened yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

def main():
    birthdate_str = input("Enter your birth date (YYYY-MM-DD): ")
    try:
        # Convert string to datetime object
        birth_date = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        age = calculate_age(birth_date)
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid date format! Please enter your birth date in YYYY-MM-DD format.")

if __name__ == "__main__":
    main()
