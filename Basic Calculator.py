# Basic calculator in Python

num1 = float(input("Enter your first number: "))
operator = input("Enter the operator: ")
num2 = float(input("Enter your second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "^":
    print(num1 ** num2)
else:
    print("You have entered the wrong operator!")

