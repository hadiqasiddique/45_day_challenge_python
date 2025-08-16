import string

def password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    upper_criteria = any(char.isupper() for char in password)
    lower_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_criteria = any(char in string.punctuation for char in password)

    # Store results in a dictionary
    strength = {
        "length": length_criteria,
        "uppercase": upper_criteria,
        "lowercase": lower_criteria,
        "digits": digit_criteria,
        "special_characters": special_criteria
    }

    # Determine overall strength
    if all(strength.values()):
        return "Strong Password", strength
    elif any(strength.values()):
        return "Moderate Password", strength
    else:
        return "Weak Password", strength

def main():
    print("Welcome to Password Strength Checker")
    print("-" * 40)

    while True:
        password = input("Enter a password to check its strength (or type 'exit' to quit): ")
        if password.lower() == "exit":
            break

        strength_text, strength_dict = password_strength(password)
        print(f"\nPassword Strength: {strength_text}")
        print("Criteria Met:")

        for criteria, met in strength_dict.items():
            print(f"{criteria.capitalize()}: {'Yes' if met else 'No'}")
        print("-" * 40)

if __name__ == "__main__":
    main()
