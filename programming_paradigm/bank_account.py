class BankAccount:
    """
    A class to represent a bank account with basic operations.
    """
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance.
        :param initial_balance: Starting balance (default is 0).
        """
        self.__account_balance = initial_balance  # Encapsulated account balance

    def deposit(self, amount):
        """
        Add the specified amount to the account balance.
        :param amount: Amount to deposit (must be positive).
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deduct the specified amount from the account balance if sufficient funds exist.
        :param amount: Amount to withdraw.
        :return: True if withdrawal is successful, False otherwise.
        """
        if amount > self.__account_balance:
            return False  # Insufficient funds
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        else:
            self.__account_balance -= amount
            return True

    def display_balance(self):
        """
        Print the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
