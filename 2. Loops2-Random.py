# Libraries in Python needs to imported so we can use the different features
# Random - create a random choices

# Exercise 1: Place in variable list = "Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca", "CoronaVac"
import random

vaccines = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca", "CoronaVac"]

random.shuffle(vaccines) # select random in shuffles
print(vaccines)
# Output: ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca", "CoronaVac"]

lucky = random.choice(vaccines) # select random in choices, need to put in variable
print(lucky)
# Output: CoronaVac



# Exercise 2: 
# a. Print successful if the value is the same 
# b. If not print fail

for vac in vaccines: # this means for each vac(element) in vaccines
    print("###################################################")
    if vac == lucky: # if vac(element) == lucky(random.choice)
        print(f"{lucky} vaccines, test successful") # f includes the variable and the strings
        print("###################################################")
        print()
        continue
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX") # if vac(element) is not equal to lucky(random.choice)
    print("Test failed")
    print()



