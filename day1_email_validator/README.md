Email Validator
A simple Python script that validates an email address using regular expressions.

Features:
Validates Email Format – Checks if an email address follows the correct format.
User Input Prompt – Accepts email address directly from the console.
Regex-Based Validation – Uses a regular expression for accuracy.

How It Works:
The program prompts the user to enter an email address.
The email is checked against a predefined regex pattern:
Username part: letters, digits, dots, underscores, %, +, -
Domain part: letters, digits, and hyphens
Must contain @ and a valid domain extension.
Displays whether the email is valid or invalid.

Example Usage:
Enter an email address: example@gmail.com
The email is valid

Enter an email address: wrong@.com
The email is invalid

Technologies Used:
Python 3
Regular Expressions (re module)