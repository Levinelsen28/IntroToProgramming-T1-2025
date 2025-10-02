def add(x, y):
    print(float(x) + float(y))

def sub(x, y):
    print(float(x) - float(y))

def multi(x, y):
    print(float(x) * float(y))

def divide(x, y):
    print(float(x) / float(y))

def expon(x, y):
    print(int(x) ** int(y))

def mod(x, y):
    print(float(x) % float(y))

def floor_divide(x, y):
    print(float(x) // float(y))

add_x = input("Give me a number for to add?\n>")
add_y = input("Give me a number for to add?\n>")
add(add_x, add_y)
sub_x = input("Give me a number for to subract?\n>")
sub_y =input("Give me a number for to subtract?\n>")
sub(sub_x, sub_y)
multi_x = input("Give me a number for to mulitpy by?\n>")
multi_y = input("Give me a number for multipy by?\n>")
multi(multi_x, multi_y)
divide_x = input("Give me a number for divide by?\n>")
divide_y =input("Give me a number for divide by?\n>")
divide(divide_x, divide_y)
expon_x = input("Give me a number for to use for a exponents?\n>")
expon_y = input("Give me a number for to use for a exponents?\n>")
expon(expon_x, expon_y)
mod_x = input("Give me a number for modulus?\n>")
mod_y = input("Give me a number for modulus?\n>")
mod(mod_x, mod_y)
floor_divide_x = input("Give me a number for floor divide?\n>")
floor_divide_y = input("Give me a number floor divide?\n>")
floor_divide(floor_divide_x, floor_divide_y)

