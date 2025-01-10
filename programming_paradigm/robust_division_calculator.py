def safe_divide(numerator, denominator):
    """
    Perform division and handle errors like ZeroDivisionError and ValueError.
    :param numerator: The numerator (as a string, to handle non-numeric inputs).
    :param denominator: The denominator (as a string, to handle non-numeric inputs).
    :return: Result of division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division and handle ZeroDivisionError
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
