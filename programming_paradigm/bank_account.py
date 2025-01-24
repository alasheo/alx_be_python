class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount with an optional initial balance.
        """
        self.__account_balance = initial_balance  # Fixed typo

    def deposit(self, amount):
        """
        Add the specified amount to the account balance.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deduct the specified amount from the account balance if sufficient funds are available.
        Returns True if the withdrawal is successful, otherwise False.
        """
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

# Example usage
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
account.display_balance()
