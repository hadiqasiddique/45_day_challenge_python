# Armstrong Number Checker
## 📌 Project Overview
This Python program checks whether a given number is an **Armstrong number** (also called a *narcissistic number*).  
An Armstrong number is a number that is **equal to the sum of its own digits each raised to the power of the number of digits**.

### Example
- **153** → `1³ + 5³ + 3³ = 153` ✅ Armstrong number  
- **9474** → `9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474` ✅ Armstrong number  
- **123** → `1³ + 2³ + 3³ = 36` ❌ Not Armstrong number  

---

## 🛠 Features
- Check if a number is an Armstrong number.
- Loop for continuous checking until the user quits.
- User-friendly input and output messages.
- Error handling for invalid inputs.

---

## 📚 Python Concepts Used
- **Loops** – To repeatedly check multiple numbers.
- **Functions** – `is_armstrong_number()` for checking.
- **List comprehension** – To calculate sum of digit powers.
- **Exception handling** – For invalid (non-numeric) inputs.
- **String methods** – `.strip()` and `.lower()` for clean input.

---

## ▶ How to Run
1. Ensure you have **Python 3.6+** installed.
2. Save the Python code to a file, for example:  
   ```bash
   armstrong_checker.py
3. Open a terminal and run:
python armstrong_checker.py

4. sFollow the prompts to enter numbers or type Q to quit.