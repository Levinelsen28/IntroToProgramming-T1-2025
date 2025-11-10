"""
1. Create a loop that prints numbers from 1 to 20, but use `break` to stop the loop when you reach 15.
2. Write a program that uses a loop to print only the odd numbers from 1 to 30, utilizing the `continue` statement.
3. Implement a loop with the `pass` statement in place of a future feature, and explain what the intended feature would be.
4. Modify a loop that counts down from 10 to 1, skipping the number 5 using the `continue` statement.
5. Create a program that sums all numbers in a list but stops adding when it encounters a negative number using the `break` statement.
"""

# Loop control statements
# Allow you to change how loops operate
# Do things like quit the loop early, skip the current loop, and even do nothing
# break, continue, and pass
# happens immediately when ran
# program continues where the loop ended
# break
# exits a loop prematurely, before it was supposed to end
# Example 1: Using break to stop the loop when reaching 15
for number in range(1, 21):
    if number == 15:
        break
    print(number)

# Continue
# Skips the current loop
# It does not exit the entire loop, just moves on to the next iteration
# Example 2: Using continue to print only odd numbers from 1 to 30
for number in range(1, 31):
    if number % 2 == 0:
        continue
    print(number)
# Pass
# Does nothing
# Usually used as a placeholder while writing code
# Example 3: Using pass as a placeholder for a future feature
if True:
    pass  # Intended feature: Implement a user authentication system here
def future_feature():
    pass  # Intended feature: Add functionality to process user data here
# Example 4: Counting down from 10 to 1, skipping the number 5
for number in range(10, 0, -1):
    if number == 5:
        continue
    print(number)
# Example 5: Summing numbers in a list, stopping at the first negative number
numbers = [10, 20, 30, -5, 40, 50]
total_sum = 0
for number in numbers:
    if number < 0:
        break
    total_sum += number
print("Total sum until negative number:", total_sum)
