import time
for i in range(10):
    print("Countdown: " + str(10 - i))
    time.sleep(1)

print()

sum = 0
integers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
for i in range(0, len(integers)):
    sum += integers[i]
print("The sum is: " + str(sum))


print()

integer_list = [1, 2, 3, 4, 5]
for i in range(len(integer_list)):
    integer_list[i] = integer_list[i] * 2
print(integer_list)

print()

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    squared = numbers[i] ** 2
    print(f"{numbers[i]} squared is {squared}")

print()
#Ask the user to enter a string. 
#Use a for loop to count
#Print the number of vowels (a, e, i, o, u) in the string.

user_string = input("Enter a string: \n>")
vowel_count = 0
vowels = "aeiouAEIOU"
for i in range(len(user_string)):
    if user_string[i] in vowels:
        vowel_count += 1

print(user_string + " has " + str(vowel_count) + " vowels.")

num = int(input("Enter a number to show its multiplication table: \n>"))
limit = input("Enter the table limit (default 10): \n>")
try:
    limit = int(limit) if limit.strip() else 10
except ValueError:
    limit = 10

for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")

print()

Names = ["Alice", "Bob", "Charlie", "Diana"]
for i in range(len(Names)):
    print(f"Hello, {Names[i]}!")