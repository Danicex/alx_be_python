def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        

        if choice == '1':
            item = input("Enter the name of the item to add: ").strip()  # Prompt for item name and strip extra spaces
            if item:  # Check if the input is not empty
                shopping_list.append(item)  # Add the item to the shopping list
                print(f'"{item}" has been added to the shopping list.')  # Confirm the addition
            else:
                print("Item name cannot be empty.")
                pass
        elif choice == '2':
            item = input("Enter the name of the item to remove: ").strip()  # Prompt for item name and strip extra spaces
            if item in shopping_list:  # Check if the item exists in the list
                shopping_list.remove(item)  # Remove the item from the shopping list
                print(f'"{item}" has been removed from the shopping list.')  # Confirm the removal
            else:
                print(f'"{item}" is not in the shopping list.')  # Inform the user if the item is not found

            pass
        elif choice == '3':
            if shopping_list:  # Check if the shopping list is not empty
                print("\nCurrent Shopping List:")  # Display the list header
                for i, item in enumerate(shopping_list, 1):  # Enumerate over the list, starting at 1
                    print(f"{i}. {item}")  # Print each item with its index
            else:
                print("The shopping list is empty.")  # Inform the user if the list has no items

            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()