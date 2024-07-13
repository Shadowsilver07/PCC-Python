# IF Condition

# True
x = 21

if x < 30:
    print("Inside If block")
    print("X is less than 30")

print("Rest of the code.")

# False



# IF/Else Condition
x = 31

if x < 30:
    print("Inside If block")
    print("X is less than 30")
else:
    print("Inside If block")
    print("X is less than 30")


# IF/Elif/Else Condition
x = 40

if x < 40: # False
    print("X is greater than 40")
elif x == 40: # True
    print("X is equal to 40")
else:
    print("X is less than 40")

# Activity
# Score = 95

# if 
    # A
# elif 
    # B
# elif 
    # C
# elif 
    # D
# else
    # F


# Output:
# For a score of 95, the grade is: A


score = 95

if score >= 95:
    print(f"For a score of", score, "the grade is: A")
elif score > 90:
    print(f"For a score of", score, "the grade is: B")
elif score > 85:
    print(f"For a score of", score, "the grade is: C")
elif score > 80:
    print(f"For a score of", score, "the grade is: D")
else:
    print(f"For a score of", score, "the grade is: F")
