class BankAccount:
    def __init__(self, account_holder, balance=0):
        # Initialize account details
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient balance or invalid amount!")

    def display_balance(self):
        """Display current account balance"""
        print(f"{self.account_holder}'s account balance: ₹{self.balance}")

# Example usage
account1 = BankAccount("Harsh Raj", 5000)
account1.deposit(1500)
account1.withdraw(2000)
account1.display_balance()
