# 📝 Word Occurrence Counter – Python Project

## 📌 Overview
The **Word Occurrence Counter** is a Python program that analyzes a given sentence (or paragraph) and counts how many times each unique word appears.  
This implementation is **case-insensitive**, **punctuation-aware**, and produces **clean, aligned output** for better readability.

This tool is a practical introduction to **text analysis** and **string processing**, with applications in:
- Data preprocessing for **Natural Language Processing (NLP)**
- Word frequency analysis in articles, books, or logs
- Educational programming practice

---

## ✨ Features
- **Case-insensitive** word counting (`"Python"` and `"python"` are treated as the same).
- **Punctuation handling** – `"example,"` and `"example"` are counted as one word.
- **Alphabetical output** for organized readability.
- **Clean, tabular display** of results.
- **Optimized counting** using Python’s `collections.Counter`.
- **Lightweight** – no external dependencies other than Python standard library.

---

## 🛠 Technologies Used
- **Python 3.x**
- `re` module – Regular expressions for text cleaning.
- `collections.Counter` – Efficient word frequency counting.

---

## 📚 Python Concepts Covered
- **String Manipulation**: lowercase conversion, tokenization.
- **Regular Expressions**: extracting clean word tokens.
- **Dictionaries & Counter**: efficient data storage and counting.
- **Loops & Sorting**: iterating and organizing output.
- **Formatted Output**: aligning columns for clean display.
- **Functions & Modular Code**: reusable components with clear docstrings.

---
 Example Usage
Input:
Enter a sentence to count the word occurrences: This is an example. This example is simple!
Output:
Word Occurrences:
------------------------------
an              1
example         2
is              2
simple          1
this            2
------------------------------
