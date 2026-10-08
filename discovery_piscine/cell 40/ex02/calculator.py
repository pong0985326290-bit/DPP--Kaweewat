#!/usr/bin/env python3

number = input("Please give me the first number : ").strip()
number2 = input("Please give me the second number : ").strip()

print("Thank you!")
print(number + " + " + number2 + " = " + str(int(number) + int(number2)))
print(number + " - " + number2 + " = " + str(int(number) - int(number2)))
print(number + " ÷ " + number2 + " = " + str(int(number) / int(number2)))
print(number + " x " + number2 + " = " + str(int(number) * int(number2)))