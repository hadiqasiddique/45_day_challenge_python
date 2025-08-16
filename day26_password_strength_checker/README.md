# Password Strength Checker 🛡️

## Project Overview
The **Password Strength Checker** is a Python program that evaluates the security of user passwords.  
It checks for **length** and **character variety** to determine if a password is **strong, moderate, or weak**.  
This tool helps users create more secure and robust passwords.

---

## Key Features
- **Length Check:** Ensures password is at least 8 characters long.  
- **Character Variety Check:** Evaluates the presence of:
  - Uppercase letters  
  - Lowercase letters  
  - Digits  
  - Special characters (`!@#$%^&*()_+…`)  
- **Comprehensive Evaluation:** Combines all criteria to provide an overall password strength assessment.

---

## Python Concepts Covered
- String manipulation  
- Conditional statements (`if-else`)  
- Loops (`for`, `while`)  
- User input handling (`input`)  
- Dictionary usage  
- Built-in functions: `any()`, `all()`, `len()`, `string.punctuation`  

---

## Modules Used
- `string` – For checking special characters easily.  
- Built-in Python functions – `input()`, `print()`, `any()`, `all()`, `len()`  

---

## How It Works
1. User enters a password.  
2. The program checks:
   - Minimum length  
   - Uppercase letters  
   - Lowercase letters  
   - Digits  
   - Special characters  
3. Password strength is displayed as **Strong**, **Moderate**, or **Weak**.  
4. Each criterion shows whether it is met (**Yes/No**).  
5. User can check multiple passwords until typing `exit`.

---

## Usage
1. Clone or download this repository.  
2. Run the Python script:
   ```bash
   python password_strength_check
3. Enter passwords to check their strength.
4. Type exit to quit the program.

## Example Output

Welcome to Password Strength Checker
----------------------------------------
Enter a password to check its strength (or type 'exit' to quit): MyPass123!

Password Strength: Strong Password

Criteria Met:

Length: Yes

Uppercase: Yes

Lowercase: Yes

Digits: Yes

Special_characters: Yes
----------------------------------------
