# daily_reminder.py

def daily_reminder():
    # Prompt for task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Validate priority input
    match priority:
        case "high":
            priority_message = f"'{task}' is a high priority task"
        case "medium":
            priority_message = f"'{task}' is a medium priority task"
        case "low":
            priority_message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
            return

    # Check if task is time-bound
    if time_bound == "yes":
        priority_message += " that requires immediate attention today!"

    # Final reminder
    print("\nReminder:", priority_message)

# Run the program
if __name__ == "__main__":
    daily_reminder()
