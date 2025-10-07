'''
3.1 boolean Expression
'''
'''
# Boolean Expressions

# Kinda like a mathematical formula

# 14 + 10 = 24  Algebra uses arithmetic operators

# + - / * ** % //

# Can only evaluate to True or False

# 5 > 10 = False    Boolean Algebra uses comparison operators

# > < >= <= == !=


print(14 + 10)  #Algebra

print(5 > 10)   #Boolean Algebra


x = 6    # SET x equal to 5, tell it what to be

print(x == 6)    # GET x equals 5, ask a question


# This is the PERFECT test question

# What is the difference between = and == ?


print(4 >= 2)    # True

print(1993 == 1993)  # True

print(-90 < -99)    # False

print(10 != 10)      # False, "not"


# Boolean expressions quiz!

answer_one = input("Give me an integer that is negative\\n>")

answer_one = int(answer_one)

print(answer_one < 0)


answer_two = input("Write the number 5\\n>")

print(answer_two == "5")


print("Walrus" + "Walrus")  #    WalrusWalrus

print("Walrus" == "Walrus") #    True
'''


print(5 > 10)
# values: 5, 10
# realtional operator: >



x = "blue"
print(x == "yellow")
# values: x, "yellow"
# realtional operator: ==


answer = "cube"
count = 1
print(answer == "cube" and count < 10)
# values: answer, "cube", count, 10
# realtional operators: ==, <
# logical operators: and
