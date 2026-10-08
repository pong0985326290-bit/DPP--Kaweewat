#!/usr/bin/env python3
num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
result = num1 * num2
print(f"{num1} x {num2} = {result}")
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")