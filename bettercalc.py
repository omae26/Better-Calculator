# 1/05/2025
# An improved calculator that allows the user to add, multiply, subtract, and divide.
# It also allows the user to select the kind of operation they want to perfrom.
# It also makes use of if statements

# Create 3 variables to store 2 numbers, and the operator the user wants to use
# We have to convert the user's input into a number, so we can perform calculations on it.
# This is because the input function always returns a string.
# num1 = input("Enter first number: "). Below is an immediate conversion.
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

# Now we can use if statements to check which operator the user wants to use.
# == means equals to
if op == "+":
    print(num1 +num2)
elif op == "-":
    print(num1 -num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")
