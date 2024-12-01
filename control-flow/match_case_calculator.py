# match_case_calculator.py

# Get input from the user
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

operation = input('Choose the operation (+, -, *, /): ')

# Use a match statement to evaluate the operator
match operation:
    case "+":
        print(f'The result is {num1 + num2}')
    case "-":
        print(f'The result is {num1 - num2}')
    case "*":
        print(f'The result is {num1 * num2}')
    case "/":
        if num2 == 0:  # Check for division by zero
            print("Division by zero is not allowed.")
        else:
            print(f'The result is {num1 / num2}')
    case _:
        print(f'Invalid operator: {operation}')
