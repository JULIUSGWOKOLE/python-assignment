# Basic Calculator Program

def calculator():
    # Ask the user for input
    num1 = float(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation. Please use +, -, *, or /.")
        return

    # Display the result
    print(f"{num1} {operation} {num2} = {result}")

# Run the calculator
calculator()