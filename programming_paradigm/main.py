import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to interact with the user via command line arguments.
    Expects two arguments: numerator and denominator.
    """
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]       # First command line argument (numerator)
    denominator = sys.argv[2]     # Second command line argument (denominator)

    # Call safe_divide and print the result
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()