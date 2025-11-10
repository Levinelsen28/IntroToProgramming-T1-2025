'''
#There are a couple types of loops in python
# The for loop lets your iterate a list
# -great for looping a set number of times
# BUT WHAT IF we need to loop an uncertain number of times???
# ex. Entering your password
# You could get it right the first time
# It could take you a million tries
# Or anything in between

real_pass = "potato45"
entered_pass = ""

attempts = 0

# A while loop continues looping until the condition is no longer True
while real_pass != entered_pass:    # Check if the entered password matches the real one
    # Ask for the password
    entered_pass = input("Please enter the password\n>")
    attempts = attempts + 1

    #Check if password is correct
    if entered_pass == real_pass:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        print(str(attempts) + " attempts.")
        print("try again...")

#End password checking
print("Welcome!")


# Whith while loops, you need be careful for infinite loops
# When you put your computer in rest mode, it has nightmares about infinite loops /joke
# An infinite loop happens when you enter a while loop that can never be escaped.
# example

#count = 0
#while True:
#    count += 1
#    print(count)

#print("All done")

# Real World Example:
# "Type "exit" to quit

user_input = ""

while user_input != "exit":
    user_input = input("Enter something (type 'exit' to quit)")
    print("You entered: " + user_input)

print("All done")
'''
#There are a couple types of loops in python
# The for loop lets your iterate a list
# -great for looping a set number of times
# BUT WHAT IF we need to loop an uncertain number of times???
# ex. Entering your password
# You could get it right the first time
# It could take you a million tries
# Or anything in between
real_pass = "potato45"
entered_pass = ""
attempts = 0
# A while loop continues looping until the condition is no longer True
while real_pass != entered_pass:    # Check if the entered password matches the real one
    # Ask for the password
    entered_pass = input("Please enter the password\n>")
    attempts = attempts + 1

    #Check if password is correct
    if entered_pass == real_pass:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        print(str(attempts) + " attempts.")
        print("try again...")
#End password checking
print("Welcome!")
# Whith while loops, you need be careful for infinite loops
# When you put your computer in rest mode, it has nightmares about infinite loops /joke
# An infinite loop happens when you enter a while loop that can never be escaped.
# example
#count = 0
#while True:
#    count += 1
#    print(count)
#print("All done")
# Real World Example:
# "Type "exit" to quit
user_input = ""
while user_input != "exit":
    user_input = input("Enter something (type 'exit' to quit)")
    print("You entered: " + user_input)
print("All done")
#While loops are very useful for situations where the number of iterations is not known beforehand.
while False:
    print("This will not be printed")
#Example: A simple counter
# code to repeat
counter = 1
while counter <= 5:
    print(counter)
    counter += 1  # Increment the counter
#An infinite loop example (be careful with these!)

while True:
    print("This loop will run forever!")
    break  # Use break to exit the loop
#To avoid infinite loops, ensure that the loop's condition will eventually become False.
#You can use break and continue statements to control the flow of while loops.

    
counter = 1
while counter <= 10:
    print(counter)
    if counter == 5:
        break  # Exit the loop when counter reaches 5
    counter += 1


counter = 0
while counter < 5:
    counter += 1
    if counter == 3:
        continue  # Skip the rest of the loop when counter is 3
    print(counter)


user_input = ""
while user_input.lower() != "exit":
    user_input = input("Enter something (type 'exit' to quit): ")
    print("You entered:", user_input)
#Nested while loops allow you to have a while loop inside another while loop.


i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1

num = 0
continue_adding = True

while continue_adding == True:
    num += 1
    print(num)
    ask = input("Do you want to cantinue? (Y/N)\n>")
    if ask.lower() != 'n':
        continue_adding = False


