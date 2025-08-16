# Personal Diary (Python, CLI)

A reliable, minimal command-line **Personal Diary** that stores **timestamped**, UTF-8 text entries in a single file. Built with the Python standard library only.

---

## Features

- **Write entries**: Add multi-line diary entries.
- **Timestamps**: Each entry is stamped with local time (`YYYY-MM-DD HH:MM:SS`).
- **View entries**: Display the full diary in chronological order.
- **Plain text storage**: Simple `diary.txt` file (easy to back up or version-control).
- **No dependencies**: Only `os` and `datetime` from the standard library.

---

## Requirements

- Python **3.7+** (tested on 3.7–3.12)

- A terminal/shell (Windows, macOS, Linux)

---
You will see a menu:
Personal Diary
1) Write a new entry
2) View past entries
3) Exit
Enter your choice (1-3):
1) Write a new entry
Type multiple lines. Press Enter on an empty line to finish.

2) View past entries
Prints the contents of diary.txt.

3) Exit
