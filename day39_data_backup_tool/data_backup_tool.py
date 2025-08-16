import os
import shutil

def specify_files():
    """Allows user to specify multiple files to backup.
    Returns:
        list: List of valid file paths."""
    files = []
    print("Enter file paths to backup (type 'done' to finish):")
    
    while True:
        file_path = input("> ").strip()
        
        if file_path.lower() == 'done':
            break
        elif os.path.exists(file_path):
            files.append(file_path)
        else:
            print(f"File '{file_path}' does not exist. Please enter a valid file path.")
    
    return files

def backup_files(files, backup_location):
    """Copies specified files to the backup directory.
    Args:
        files (list): List of file paths to backup.
        backup_location (str): Directory where files will be backed up."""
    if not os.path.exists(backup_location):
        os.makedirs(backup_location)
    
    for file in files:
        try:
            shutil.copy(file, backup_location)
            print(f"File '{os.path.basename(file)}' copied successfully to backup.")
        except Exception as e:
            print(f"Error copying '{file}': {e}")

def main():
    files = specify_files()
    
    if not files:
        print("No files specified for backup. Exiting.")
        return
    
    backup_location = input("Enter the backup location:\n> ").strip()
    backup_files(files, backup_location)

if __name__ == "__main__":
    main()
