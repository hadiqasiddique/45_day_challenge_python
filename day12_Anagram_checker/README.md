# Python Anagram Checker

## Project Overview
The Anagram Checker is a Python program that checks whether two given strings are anagrams of each other.

An **anagram** is a word or phrase formed by rearranging the letters of another.  
Example: "cinema" and "iceman", "listen" and "silent".

By the end of this project, we will have a solid understanding of:
- String manipulation in Python
- Handling user input
- Using built-in Python functions for string operations

---

## **Key Features**
1. **User Input:** Accepts two strings from the user.
2. **Sanitize Input:** Removes spaces and converts strings to lowercase.
3. **Anagram Check:** Compares sorted versions of the sanitized strings.
4. **Interactive Output:** Prints if the strings are anagrams or not.

---

## **Python Concepts Covered**
- String manipulation (`lower()`, `split()`, `join()`)
- User input (`input()`)
- Conditional statements (`if-else`)
- Functions and modular programming
- Sorting with `sorted()`

---

## **How to Run**
1. Ensure Python is installed on your system.
2. Save the code as `anagram_checker.py`.
3. Run the program:
   ```bash
   python anagram_checker.py

**Example:**

- Enter your first string: listen

- Enter your second string: silent

Output: listen and silent are anagrams!

- Enter your first string: hello

- Enter your second string: world

Output: hello and world are not anagrams.