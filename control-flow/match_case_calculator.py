# Get input from the user
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

operator = input('Choose the operation (+, -, *, /): ')

# Use a match statement to evaluate the operator
match operator:
    case "+":
        print(f'{num1} + {num2} = {num1 + num2}')
    case "-":
        print(f'{num1} - {num2} = {num1 - num2}')
    case "/":
       print(f'{num1} / {num2} = {num1 / num2}')
    case "*":
        print(f'{num1} * {num2} = {num1 * num2}')
    case _:
        print(f'Invalid operator: {operator}')
