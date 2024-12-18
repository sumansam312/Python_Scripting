# Python script for a simple calculator

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    return x / y

# Input values
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Select operation
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation based on user choice
if operation == "+":
    print(f"The result is: {add(num1, num2)}")
elif operation == "-":
    print(f"The result is: {subtract(num1, num2)}")
elif operation == "*":
    print(f"The result is: {multiply(num1, num2)}")
elif operation == "/":
    print(f"The result is: {divide(num1, num2)}")
else:
    print("Invalid operation!")
