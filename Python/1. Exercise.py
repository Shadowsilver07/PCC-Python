# This is a comment

"""
Write a progaram to count the number of even and odd numbers from a series of numbers.
Sample Numbers:
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output:
Number of even numbers: 4
Number of odd numbers: 5
"""

""" 
1. - Mine
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
a = 0
b = 0

for num in numbers: 
    if num % 2 == 0:
        a += 1
    else: 
        b += 1

print("Number of even numbers1:", a)
print("Number of odd numbers:", b)

--------------------
2. - Correct!
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
a = 0  # initialize counter for even numbers
b = 0  # initialize counter for odd numbers

for num in numbers:  # iterate over the tuple
    if num % 2 == 0:
        a += 1  # increment even counter
    else:
        b += 1  # increment odd counter

print("Number of even numbers:", a)
print("Number of odd numbers:", b)

"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
a = 0
b = 0

for num in numbers:
    if num % 2 == 0:
        a += 1
        print("This is inside the loop and keeps on iterating--")
    else: 
        b += 1
    print("This is inside the loop and keeps on iterating")

print("Number of even numbers:", a)
print("Number of odd numbers:", b)

