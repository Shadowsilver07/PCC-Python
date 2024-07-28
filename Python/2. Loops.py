# Iteration - same concept for other Programming languages - use for repetitive task  - countable numbers in sequence
# iterates in sequence
# For Loop

planet = "Earth"

for i in planet:
    print("Value is now ",i)

# Activity
# Output:

# apple
# banana
# cherry

fruit = ["apple", "banana", "cherry"]

for i in fruit:
    print(i)

vaccines = ("Moderna", "Pfizer", "Sputnik", "Covaxin", "AztraZeneca")

for vac in vaccines:
    print(f"{vac} vaccinne provides Immunization against covid19")

name = "Mary"    
age = 18
print(f"Name: {name}\nAge: {age}")


# While Loop - cont to execute as long as the given condition is true

x = 0

while x <= 10:
    print("Value of X is :", x)
    #print("Looping") - optional
    x += 1


# Activity
# Output:
# Count is 2
# Count is 3
# Count is 4
# Count is 5

# Output (bonus) - The sum of numbers from 2 to 11 is: 65

x = 1

while x <= 4:
    x += 1
    print("Count is ", x)


x = 2
sum = 0
while x <= 11:
    sum += x
    x += 1
print("The sum of numbers from 2 to 11 is:", sum)


