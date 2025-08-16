
import os
from cryptography.fernet import Fernet, InvalidToken

KEY_FILE = "secret.key"
STORE_FILE = "passwords.txt"

# ---------- Key Management ----------

def generate_key():
    """
    Generate a new Fernet key and save it to KEY_FILE (binary).
    """
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    """
    Load and return the Fernet key from KEY_FILE.
    """
    with open(KEY_FILE, "rb") as f:
        return f.read()

# ---------- Crypto Helpers ----------

def encrypt_message(message: str) -> bytes:
    """
    Encrypt a plaintext string and return the token (bytes).
    """
    key = load_key()
    f = Fernet(key)
    return f.encrypt(message.encode("utf-8"))

def decrypt_message(token: bytes) -> str:
    """
    Decrypt a token (bytes) and return the plaintext string.
    """
    key = load_key()
    f = Fernet(key)
    plaintext = f.decrypt(token)
    return plaintext.decode("utf-8")

# ---------- Main Program ----------

def main():
    # Ensure we have a key file
    if not os.path.exists(KEY_FILE):
        generate_key()

    # In-memory cache (optional convenience)
    passwords = {}  # service -> token (bytes)

    while True:
        print("\n=== Password Manager ===")
        print("1. Add New Password")
        print("2. Retrieve a Password")
        print("3. Exit")

        # Get menu choice
        try:
            ch = int(input("Enter your choice: ").strip())
        except ValueError:
            print("Invalid input! Please enter 1, 2, or 3.")
            continue

        if ch == 1:
            # Add new password
            service = input("Enter the service: ").strip()
            password = input("Enter your password: ")

            if not service:
                print("Service name cannot be empty.")
                continue

            try:
                token = encrypt_message(password)  # bytes
            except Exception as e:
                print(f"Encryption failed: {e}")
                continue

            passwords[service] = token

            # Persist to file as service:token\n (token base64-safe text)
            try:
                with open(STORE_FILE, "a", encoding="utf-8") as f:
                    f.write(f"{service}:{token.decode('utf-8')}\n")
                print("Password added successfully.")
            except Exception as e:
                print(f"Failed to save password: {e}")

        elif ch == 2:
            # Retrieve existing password
            service = input("Enter the service name to retrieve the password: ").strip()
            if not service:
                print("Service name cannot be empty.")
                continue

            token = None

            # 1) Check in-memory cache first
            if service in passwords:
                token = passwords[service]
            else:
                # 2) Fallback to file search
                if not os.path.exists(STORE_FILE):
                    print("No passwords have been saved yet.")
                    continue

                try:
                    with open(STORE_FILE, "r", encoding="utf-8") as f:
                        for line in f:
                            line = line.strip()
                            if not line or ":" not in line:
                                continue
                            stored_service, stored_token_text = line.split(":", 1)
                            if stored_service == service:
                                token = stored_token_text.encode("utf-8")
                                break
                except Exception as e:
                    print(f"Failed to read store: {e}")
                    continue

            if token is None:
                print("Service not found.")
                continue

            # Decrypt and show
            try:
                plaintext = decrypt_message(token)
                print(f"Password for '{service}' is: {plaintext}")
            except InvalidToken:
                print("Decryption failed: invalid token or wrong key file.")
            except Exception as e:
                print(f"Decryption error: {e}")

        elif ch == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
