# def is used to define a function
# we find this in complex codes 
# take 1 parameter when we are defining 
# allows you to encapsulate a block of codes
# def my_function():
# instead of repeating the codes - easier way is to just call out the function.

def print_hi(name): # where name is the parameter, 
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')


"""

if __name__ == '__main__':

__name__ is a built-in Python variable that holds the name of the current module.
__main__ is a special value that indicates that the script is being run directly (i.e., not being imported as a module by another script).
The code inside this block will only be executed if the script is run directly (i.e., not imported as a module).

In summary, this code defines a function print_hi that takes a name parameter and prints a greeting message with the name. 
The if __name__ == '__main__': block ensures that the function is only called when the script is run directly, and it passes the string 'PyCharm' as the name parameter.

"""