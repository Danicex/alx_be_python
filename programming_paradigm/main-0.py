import sys
from bank_account import BankAccount

def main():
    """
    Main function to interact with the BankAccount class via command-line arguments.
    """
    account = BankAccount(100)  # Example starting balance

    # Ensure at least one command is passed
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and optional amount
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Handle the commands
    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "withdraw" and amount is not None:
        try:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Use: deposit:<amount>, withdraw:<amount>, or display.")

if __name__ == "__main__":
    main()
