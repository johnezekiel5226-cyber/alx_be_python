class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated attribute
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")

# Example usage:
account = BankAccount(120)
account.deposit(67.0)
account.withdraw(30)

