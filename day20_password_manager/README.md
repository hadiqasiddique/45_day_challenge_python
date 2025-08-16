# 🔐 Day 20 – Password Manager (Python)

A secure **Password Manager** built in Python using the **`cryptography`** library to encrypt and decrypt stored passwords.  
This project allows you to **generate, store, and retrieve passwords** safely.

---

## 📌 Features
- **Add new passwords** for different accounts/websites.
- **Secure storage** using `Fernet` symmetric encryption.
- **Retrieve saved passwords** by decrypting stored data.
- **Master key file** (`key.key`) is generated for encryption/decryption.
- **User-friendly CLI menu**.

---

## 🛠️ Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/python_45_day_challenge.git
   cd python_45_day_challenge/day20_password_manager
2. Install dependencies:
   pip install cryptography
3. Run the program:
  python password_manager.py

⚠️ Important Notes

Do not share your key.key file — it is required to decrypt your saved passwords.

If key.key is lost, all stored passwords will be permanently unreadable.

Use strong and unique passwords for better security.

# Example Usage
[1] Add new password
[2] View stored passwords
[3] Exit

Enter your choice: 1
Enter account name: Gmail
Enter password: MySecurePass123
✅ Password saved successfully!