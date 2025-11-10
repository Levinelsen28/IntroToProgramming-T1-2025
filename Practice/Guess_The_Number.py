#Generate a random number between 1 and 100. 
# Then use a while loop to allow the user to guess the number.
# Provide feedback on whether the guess is too high, too low, or correct.
# The loop should continue until the user guesses the correct number.
import random
number_to_guess = random.randint(1, 100)
user_guess = None
while user_guess != number_to_guess:
    user_guess = int(input("Guess a number between 1 and 100: "))
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number.")
