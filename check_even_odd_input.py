"""
This program will take one number as user input and check whether it is even or odd
"""

# user input
num = int(input(f"Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")