'''
try:
    # Code that may raise an exception
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Cannot divide by zero.")


try:
    # Code that may raise different exceptions
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

    
file = None
try:
    file = open("example.txt", "r")
    # Perform file operations
except FileNotFoundError:
    print("Error: File not found.")
finally:
    if file:
        file.close()

        
def divide(numerator, denominator):
    if denominator == 0:
        raise ValueError("Error: Cannot divide by zero.")
    return numerator / denominator

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)
'''
'''
import random


print(random.random())  # Output: e.g., 0.56432


print(random.randint(1, 10))  # Output: e.g., 7 (a number between 1 and 10)


print(random.uniform(5, 10))  # Output: e.g., 7.654 (a float between 5 and 10)


print(random.randrange(5, 10))  # Output: e.g., 9 (an integer between 5 and 10


colors = ['red', 'blue', 'green', 'yellow']
print(random.choice(colors))  # Output: e.g., 'green'


print(random.choices(colors, k=3))  # Output: e.g., ['blue', 'red', 'yellow']


print(random.sample(colors, k=2))  # Output: e.g., ['red', 'green']


deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(deck)  # Output: e.g., [3, 1, 5, 2, 4]


random.seed(42)
print(random.random())  # Output: 0.6394267984578837


import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

dice1, dice2 = roll_dice()
print("You rolled a" + str(dice1) + " and a " + str(dice2) + "!")
'''
'''
# Exception Handling
# Write a program that asks for two numbers and divides them

# if    =   try
# elif  =   except with error type
# else  =   except
def divide_two_numbers():
    try:    # We always enter the try block, there is no condition
        x = int(input("What is the first number?\n>"))
        y = int(input("What is the second number?\n>"))
        print(x / y)

    except ZeroDivisionError:
        print("Cannot divide by zero, try again.")
        divide_two_numbers()   

    except ValueError:
        print("Please enter a valid numerical symbol, try again.")
        divide_two_numbers()   

    except: # If anything in the try block causes an error,
            # the try block stops immediately and the except is ran instead
            # The rest of the try block never finishes running, its skipped
            # If the try block executes without an error, the except is skipped
            # the only way to get into the except is to "throw" an error
        print("IDK what you did, but you broke it... Try again.")
        divide_two_numbers()    # Tell the function to run again

divide_two_numbers()
'''



var = input("Enter a number\n>")


try:
    print(int(var) * 2)

except:
    print("You must enter an interger")

import random

r = random.randint(0, 10)

print(r)
