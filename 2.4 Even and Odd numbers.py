# Write a program to count the number of even and odd numbers from a series of numbers.
#   Sample NumbersL
#   numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#   Expected Output:
#   Number of even numbers: 4
#   Number of odd numbers: 5
#   Submit until 5:45 PM

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Numbers of even numbers:", even_count)
print("Numbers of odd numbers:", odd_count)