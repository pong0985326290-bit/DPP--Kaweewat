#!/usr/bin/env python3

q = str(input("Please give me a number : ").strip())

number = float(q)


if number.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")