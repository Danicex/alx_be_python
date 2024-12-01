# multiplication_table.py

def multiplication_table():
    # Prompt user for a number
    number = input("Enter a number to see its multiplication table: ").strip()

    # Validate input
    while not number.lstrip('-').isdigit():
        print("Invalid input. Please enter a valid number.")
        number = input("Enter a number to see its multiplication table: ").strip()

    number = int(number)

    # Generate and print the multiplication table
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

# Run the program
if __name__ == "__main__":
    multiplication_table()
