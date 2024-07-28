"""
- Use while loop that will keep running until the desired item is selected. 
- Once it is found, the loop will stop using break statement.

- extra: count and print 
"""

# Done 
import random

fruits = ["cherry", "strawberry", "apple", "orange"] # 1. Create a list of items
desiredItem = "apple" 
a = 0 # This is extra

while True: 
        randomItem = random.choice(fruits) # 2. Pick a random item from the list
        print(f"The random item selected is: {randomItem}")
        a += 1
        if randomItem == desiredItem: # 3. once desireditem has been selected, print then break
            print("Desired item found! Stop the loop.")
            break

print(a) # This is extra


