"""
Function                Description	                                                Example Input	                Example Output
str.upper()             Converts all characters to uppercase	                    "hello"	                        "HELLO"
str.lower()	            Converts all characters to lowercase	                    "WORLD"	                        "world"
str.capitalize()	    Capitalizes the first character	                            "python programming"	        "Python programming"
str.title()	            Capitalizes the first character of each word	            "python programming"	        "Python Programming"
str.strip()            	Removes whitespace from both ends	                        "   hello   "	                "hello"
str.replace(old, new)	Replaces occurrences of a substring	                        "hello world"	                "hello Python" (with str.replace("world", "Python"))
str.split(separator)	Splits a string into a list based on a separator	        "one,two,three"	                ["one", "two", "three"]
str.join(iterable)	    Joins elements of an iterable into a string	                ["a", "b", "c"]	                "a-b-c" (with "-".join(["a", "b", "c"]))
str.find(substring) 	Returns the index of the first occurrence of a substring	"hello"	                        1 (for str.find("e"))
str.endswith(suffix)	Checks if the string ends with a specified suffix	        "filename.txt"	                True (for str.endswith(".txt"))
"""
'''
# String functions1
# A group of like-functions that manipulate strings
# The modify strings
# SUPER easy and convenient to use
# Python would really not be fun without them

#   .lower()
# converts a string to all lowercase
# no matter what the input casing is, it is converted to lowercase
# and the answer is lowercase
input_answer = "Lord of The Rings"
input_answer = input_answer.lower() # Converts to "lord of the rings"
real_answer = "lord of the rings"
print(input_answer == real_answer)

# .upper()
# Converts a string to uppercase!
x = "hello world".upper()
print(x)    # prints "HELLO WOLRD"

# .capitalize()
# converts to lowercase, then capitalizes the first letter
y = "HeLlO wOrLd".capitalize()
print(y)    # print "Hello world"

# .title()
# converts a string to titlecase
#capital first letters of words
z = "HeLlO wOrLd".title()
print(z)    # print "Hello World"

# .swapcase()
# it inverts the casing of eac character
q = "Hello World!".swapcase()
print(q)    #prints "hELLO wORLD!"

'''
'''
# the if statement has two buddies
# the first little buddy is the the else statement

x = 10

if x > 0:   # not every if needs an else
    print("x is a postiive number")

# the second little buddy is the elif (else if)
elif x < 0:
    print("x is a negative number")

else:       # else always needs an if
    print("x is zero")



light = input("What color is the light?\n>")

if light.lower() == "green":
    print("GO")

elif light.lower() == "yellow":
    print("STOP IF SAFE")

elif light.lower() == "red":
    print("STOP")

else:
    print("YIELD")



x = 10

if x > 5:
    print("x is greater than 5")

if x > 8:
    print("x is greater than 8")

####################################
if x > 5:
    print("x is greater than 5")

elif x > 8:
    print("x is greater than 8")
'''
sentence = input("Give me a sentence?")
print(sentence.upper())
print(sentence.strip())
print(sentence.replace())

if sentence.endswith("."):
    print(True)

else:
    print(False)

coin_diameter = "dime"
deposit = 0.00

