from math import *

#adding int () converts the input into a number
num1 = int(input("Enter 1st number: "))
op = input("Enter Operator (E.g +/-)): ")
num2 = int(input("Enter 2nd number: "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
