class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        print(f"Current Balance: {self.balance}")


def main():
    acc = BankAccount()

    while True:
        print("\n=== Bank Account Manager ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Get Balance")
        print("4. Exit")

        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if ch == 1:
            amount = float(input("Enter amount to be deposited: "))
            acc.deposit(amount)
        elif ch == 2:
            amount = float(input("Enter amount to be withdrawn: "))
            acc.withdraw(amount)
        elif ch == 3:
            acc.get_balance()
        elif ch == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again")


if __name__ == "__main__":
    main()
