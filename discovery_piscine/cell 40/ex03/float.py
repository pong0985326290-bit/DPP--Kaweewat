#!/usr/bin/env python3

usr_input = str(input("Please give me a number : ").strip())

number = float(usr_input)


if number.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")