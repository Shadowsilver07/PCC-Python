# Start an infinite loop with while True.
# Print the current value of the variable (integer)
# Print "Looping".
# Double the value of the variable
# Pause for 1 second with the sleep function of time module.
# The loop will repeat these steps indefinitely until manually stopped.


import time # time related function
a = 1
while True: # 1. Start an infinite loop while
    print("The value of a is ", a)# 2. Print the value of integer
    print("Looping") # 3. Print Looping
    a *= 2 # 4. Double the value of the integer
    time.sleep(1) # 5. Pause for 1 second with the sleep function of time module.

# Press ctrl + c to stop the loop