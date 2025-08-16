# 📅 Days Between Dates Calculator

A simple Python project that calculates the number of days between two dates entered by the user.

## Features
- Accepts two dates from the user in `YYYY-MM-DD` format
- Validates the date format using **exception handling** (`try/except`)
- Calculates the difference in days using Python's `datetime` module
- Works regardless of which date comes first (always returns a positive number)

---

## Topics Covered
1. **`datetime` Module** - Used for handling dates and calculating the difference
2. **User Input** - Getting and validating user-entered dates
3. **Exception Handling** - Handling invalid formats using `try/except`
4. **Functions** - Code is organized into reusable functions

---

## How to Run
1. Save the script as `days_between_dates.py`
2. Open a terminal and run:
   ```bash
   python days_between_dates.py

3. Enter two dates in YYYY-MM-DD format:

Enter the first date (YYYY-MM-DD): 2025-05-09

Enter the second date (YYYY-MM-DD): 2025-05-19


4. The program will output:

✅ The number of days between 2025-05-09 and 2025-05-19 is 10 days.