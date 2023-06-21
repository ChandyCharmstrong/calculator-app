import os

def calculator():
    print("Welcome to the simple calculator app!")
    
    """Ask the user for two numbers and the operation"""
    # Used floats instead of int as it allows more precision 
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    op = input("Enter the operator (+, -, *, /): ")
    
    """Operators, calculations & defensive programming""" 
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Cannot divide by zero. Please try again.")
            return
        else:
            result = num1 / num2
    else:
        print("Invalid operator entered. Please try again.")
        return
    
    """Display result, write/append to a text file"""
    print(f"The answer is: {result}")
    
    """Ask the user for the filename to store the equations"""
    filename = input("Enter the filename to store the equations: ")
    
    """Create the file if it doesn't exist"""
    if not os.path.exists(filename):
        open(filename, 'w').close()
    
    with open(filename, 'a') as file:
        file.write(f"{num1} {op} {num2} = {result}\n")
        
def read_equations():
    """Ask the user for the filename to read equations from"""
    filename = input("Enter the filename to read equations from: ")
    
    if not os.path.exists(filename):
        print("File not found. Would you like to create a new file with that name?")
        create_file = input("Enter 'yes' to create a new file, or any other key to cancel: ")
        if create_file.lower() != 'yes':
            print("Operation canceled.")
            return
        else:
            open(filename, 'w').close()
    
    """Read file and print equations"""  
    with open(filename, 'r') as file:
        equations = file.readlines()
        for eq in equations:
            print(eq.strip())
    
"""Main loop"""
while True:
    print("\nWhat would you like to do?")
    print("1. Enter two numbers and an operator")
    print("2. Read equations from a file")
    print("3. Quit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        calculator()
    elif choice == '2':
        read_equations()
    elif choice == '3':
        print("Thanks for using the calculator app!")
        break
    else:
        print("Invalid choice. Please try again.")