
import os
from datetime import datetime

# ---- Configuration ---------------------

DIARY_FILE = "diary.txt"  # text file that stores all entries (UTF-8)

# ---- Core utilities -------------------

def _now_timestamp() -> str:
    """Return current local timestamp in ISO-like format."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def _ensure_file_exists(path: str) -> None:
    """Create an empty file if it doesn't exist (no-op if it does)."""
    if not os.path.exists(path):
        # Create parent dirs if a nested path is provided
        parent = os.path.dirname(path)
        if parent and not os.path.exists(parent):
            os.makedirs(parent, exist_ok=True)
        # Touch the file
        with open(path, "w", encoding="utf-8"):
            pass

# ---- Features --------------------

def write_entry() -> None:
    """
    Prompt the user for a multi-line diary entry and append it to the diary file
    with a timestamp. Entry ends when the user presses Enter on an empty line.
    """
    print("\nWrite your diary entry (press Enter on an empty line to finish):")

    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            # If input stream closes abruptly, treat as end-of-entry
            break
        if line == "":
            # End on blank line—but prevent empty entries
            if lines:
                break
            else:
                print("Entry cannot be empty. Please type something.")
                continue
        lines.append(line)

    entry_text = "\n".join(lines).strip()
    if not entry_text:
        print("No content captured. Entry discarded.")
        return

    _ensure_file_exists(DIARY_FILE)
    timestamp = _now_timestamp()

    # Use a clear, parseable block format with a separator
    block = (
        f"[{timestamp}]\n"
        f"{entry_text}\n"
        f"{'-'*40}\n"
    )

    try:
        with open(DIARY_FILE, "a", encoding="utf-8") as f:
            f.write(block)
        print("Entry saved.")
    except OSError as e:
        print(f"Failed to write entry: {e}")

def view_entries() -> None:
    """
    Display all diary entries. If the diary is empty or missing, inform the user.
    """
    if not os.path.exists(DIARY_FILE):
        print("\nNo diary entries found.")
        return

    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
    except OSError as e:
        print(f"\n Failed to read diary: {e}")
        return

    if not content:
        print("\nNo diary entries found.")
        return

    print("\n— Diary Entries —")
    print(content)
    print("— End —")

def main() -> None:
    while True:
        print("\nPersonal Diary")
        print("1) Write a new entry")
        print("2) View past entries")
        print("3) Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye.")
