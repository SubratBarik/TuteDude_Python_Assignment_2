"""
This program returns the sum of integers from 1 to 50 using loop

This can be done is two ways:
1) Creating a list of 50 items, starting from 1 to 50 ex: nums = [1,2,3...,49,50]
2) By using range()
"""
sum = 0

for i in range(1, 51):
    sum += i
print(f"The sum of the numbers from 1 to 50 is: {sum}")