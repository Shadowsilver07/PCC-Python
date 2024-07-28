import random

# Place in variable list = "Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca", "CoronaVac"

# vaccines = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca", "CoronaVac"]
""" - The shuffle
import random
random.shuffle(vaccines)
print (vaccines)

lucky = random.choice(vaccines)
print(lucky)

for vac in vaccines:
    print('#########################################')
    if vac == lucky:
        print(f"{lucky} vaccine, test successful")
        print ("########################################")
        print()
        continue
    print("XXXXXXXXXXXXXXXXXXXXXXXX")
    print("Test Failed")
    print()
"""

""" - The fruit
    fruits = ["cherry", "strawberry", "apple", "orange"]
    desiredItem = "apple"

    while True:
        randomItem = random.choice(fruits)
        print(f"The random item selected is: {randomItem}")

        if randomItem == desiredItem:
            print("Desired item found! Stop the loop.")
            break
"""

import time #time-related functions 

# Start an infinite loop with while True.
# Print the current value of the variable (integer)
# Print "Looping".
# Double the value of the variable
# Pause for 1 second with the sleep function of time module
# The loop will repeat these steps indefinitelt until manually stopped.

""" -  Mine
number = [1, 2, 3, 4, 5, 6, 7, 8]
number1 = 8
while True:

    print(f"Looping: {number}")

    if number == 8:
        break

        
"""
import time
x = 2

while True:
    print("Value of X is:", x)
    print("Looping")
    x*=2
    time.sleep(1)
    



          
