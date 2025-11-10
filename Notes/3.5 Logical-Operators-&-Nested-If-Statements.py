'''
# Nested if statements


prime = True
cost = 20
age = 17
consent = False

# if (prime == True or cost >= 25) and (age >= 18 or consent == True):

if prime:
    if age >= 18:
        print("FREE SHIPPING APPLIED!")
    elif consent:
        print("FREE SHIPPING APPLIED!")
    else:
        print("No free ship for u...")

elif cost >= 25:
    if age >= 18:
        print("FREE SHIPPING APPLIED!")
    elif consent:
        print("FREE SHIPPING APPLIED!")
    else:
        print("No free ship for u...")

else:
    print("No free ship for u...")


# Decide if we need an umbrella
# You need an umbrella if its raining AND you are going outside that day.



raining = input("Is it raining outside?\n>")

if raining.lower() == "yes":
    outside = input("Do you plan on going outside?\n>")
    
    if outside.lower("yes"):
        print("BRING AN UMBRELLA")
    else:
        print("NO UMBRELLA")
else:
    print("NO UMBRELLA")
'''







