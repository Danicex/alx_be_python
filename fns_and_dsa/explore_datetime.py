from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format as "YYYY-MM-DD HH:MM:SS"
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompt the user to enter a number of days and calculate the future date.
    """
    try:
        # Prompt the user for the number of days to add
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        
        # Calculate the future date
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number_of_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format as "YYYY-MM-DD"
        
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    # Part 1: Display the current date and time
    display_current_datetime()
    
    # Part 2: Calculate a future date
    calculate_future_date()
