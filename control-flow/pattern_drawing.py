# pattern_drawing.py

def draw_pattern():
    # Prompt user for pattern size
    size = input("Enter the size of the pattern (positive integer): ").strip()

    # Validate input
    while not size.isdigit() or int(size) <= 0:
        print("Invalid input. Please enter a positive integer.")
        size = input("Enter the size of the pattern (positive integer): ").strip()

    size = int(size)

    # Draw the square pattern
    row = 0
    while row < size:
        for _ in range(size):  # Print asterisks for one row
            print("*", end="")
        print()  # Move to the next line after printing the row
        row += 1

# Run the program
if __name__ == "__main__":
    draw_pattern()
