#!/usr/bin/env python3

tt = int(input("Enter a number less than 25\n"))
if tt > 25:
    print("Error")
else:
    while tt <= 25:
        print(f"Inside the loop, my variable is {tt}")
        tt += 18
        