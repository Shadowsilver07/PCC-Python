# This is where we gather the segragated file - (functions)
# 3 files to be connected - This is main 
# This is where we put the set of instructions

import random # This is where our library

def vac_feedback(vac, efficacy):
    print(f"{vac} Vaccine is having {efficacy} % efficacy.")
    if (efficacy > 50) and (efficacy <= 75):
        print("Seems not so effective, Needs more trial")
    elif (efficacy > 75) and (efficacy < 90):
        print("Can consider this vaccine.")
    elif efficacy >= 90:
        print("Sure, will take the shot.")
    else:
        print("Needs many more trials.")


def order_food(min_order, *args): # collects all arguments na magpapasa sa function then ipapasa sa tuple that we are going to manipulate and iterate.
    print(f"You have ordered:: {min_order}")
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 20 mins:\nEnjoy the party")

def time_activity(*args, **kwargs):
    """
    
    Input: Multiple values for minutes, key=value pair activity
    Output: Return sum of minutes + random minute spect on a random activity

    #    print(args)
    #   print(kwargs)
    min = sum(args) + random.randint(0, 60)
    #    print(min)
    choice = random.choice(list(kwargs.keys()))
    #    print(choice)
    print(f"You have to spend {min} Minutes for {kwargs[choice]}")
    time_activity(10, 20, 10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")

    """
    minutes = sum(args) + random.randint(0, 60)
    choice = random.choice(list(kwargs.keys()))
    print(f"You have to spend {minutes} Minutes for {kwargs[choice]}")
