# Data Backup Tool

## 📌Project Overview
The **Data Backup Tool** is an intermediate-level Python application designed to efficiently backup important files. Users can specify which files to backup, and the tool copies them to a specified backup directory. It also includes error handling to manage missing files or inaccessible directories.

## Features
- **File Selection:** Users can input multiple file paths to backup.
- **Backup Destination:** Users can specify a backup location.
- **Error Handling:** Alerts the user if a file does not exist or cannot be copied.
- **Automated Directory Creation:** Creates backup directories if they don’t exist.

## Python Concepts Covered
- File I/O
- String manipulation
- Loops and conditionals
- Functions and return statements
- Error handling using `try-except`
- Using built-in modules (`os`, `shutil`)

## How to Use
1. Run the program using Python.
2. Enter file paths you want to backup. Type `done` to finish.
3. Enter the backup directory where the files should be copied.
4. The program will copy the files and display confirmation messages.
5. Check the backup directory to verify the files have been copied successfully.

## Requirements
- Python 3.8+
- Standard Python libraries: `os`, `shutil`

## Example
Enter file paths to backup (type 'done' to finish):

C:\Users\Hadiqa\Documents\file1.txt

C:\Users\Hadiqa\Documents\file2.txt

done


Enter the backup location:

C:\Users\Hadiqa\Documents\Backup

File 'file1.txt' copied successfully to backup.

File 'file2.txt' copied successfully to backup.
