'''
# Loop control statements
# Allow you to change how loops operate
# Do things like quit the loop early, skip the current loop, and even do nothing
# break, continue, and pass
# happens immediately when ran
# program continues where the loop ended

# break
# exits a loop prematurely, before it was supposed to end

#Example

bag_of_fruit = ["apple", "orange", "bug", "watermelon", "pear"]

for fruit in bag_of_fruit:

    if fruit == "bug":
        print("Uh oh, you found a bug in the bag...")
        break   # the break statement exits the loop immediately and continues
    else:    
        print("You ate a " + fruit)


# Continue
# Skips the current loop
# It does not exit the entire loop, just moves on to the next iteration

#Example
orders = [15, 30, 35, 23, 100, 3, 10, 22]

# Discount applying program
# Only apply discount for orders above $20
for order in orders:
    if order < 20:
        continue    #Skips the rest if the loop iteration and goes to the next iteration
    print("$" + str(order) + " order discounted 5% to $" + str(order * 0.95))


# Pass
# Does nothing
# Usually used as a placeholder while writing code
# Text adventure project

if True:
    pass


def enter_forest():
    pass

def swim_river():
    pass

def eat_icecream():
    pass
'''

# Loop control statements
# Allow you to change how loops operate
# Do things like quit the loop early, skip the current loop, and even do nothing
# break, continue, and pass
# happens immediately when ran
# program continues where the loop ended
# break
# exits a loop prematurely, before it was supposed to end
#Example
bag_of_fruit = ["apple", "orange", "bug", "watermelon", "pear"]
for fruit in bag_of_fruit:
    if fruit == "bug":
        print("Uh oh, you found a bug in the bag...")
        break   # the break statement exits the loop immediately and continues
    else:    
        print("You ate a " + fruit)
# Continue
# Skips the current loop
# It does not exit the entire loop, just moves on to the next iteration
#Example
orders = [15, 30, 35, 23, 100, 3, 10, 22]
# Discount applying program
# Only apply discount for orders above $20
for order in orders:
    if order < 20:
        continue    #Skips the rest if the loop iteration and goes to the next iteration
    print("$" + str(order) + " order discounted 5% to $" + str(order * 0.95))
# Pass
# Does nothing
# Usually used as a placeholder while writing code
# Text adventure project
if True:
    pass
def enter_forest():
    pass
def swim_river():
    pass
def eat_icecream():
    pass

