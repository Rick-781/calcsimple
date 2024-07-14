import math

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y. Handle division by zero."""
    if y == 0:
        return "Error! Division by zero."
    return x / y




def calculator():
    """Run the calculator."""
    while True:
        display_menu()
        choice = input("Enter choice (1-9): ")

        if choice == '9':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")
            elif choice == '6':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
        elif choice == '7':
            num = float(input("Enter number for square root: "))
            print(f"√{num} = {square_root(num)}")
        elif choice == '8':
            num = int(input("Enter a non-negative integer for factorial: "))
            print(f"{num}! = {factorial(num)}")
        else:
            print("Invalid input. Please choose a valid operation.")


if __name__ == "__main__":
    calculator()
