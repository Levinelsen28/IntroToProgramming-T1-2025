'''
import random
#Python has four types of collections
#Tuple
#Set
#>List
#>Dictionary

#Today, were going to focus on listssstssttstsss
#A list is a way to store more than one vlaue in single variable
#The values in the list are called ITEMS
#Items can be access by their INDEX (position in the list) indices
#IDEX                       0                    1           2                  3            4
best_elden_ring_weapons = ["Blasphemous Blade", "Moonveil", "Rivers of Blood", "Iron Ball", "Bloodhound's Fang"]
best_years = [1776, 1985, 1994, 1957, 2016]
myint = 3

print(len(best_elden_ring_weapons))


print(best_years[0])
print(best_elden_ring_weapons[0])                                   #Print the first item
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])       #Print the last item

#List items can be changed!!!
best_elden_ring_weapons[3] = "Spiked Fist"
print(best_elden_ring_weapons)

#List functions!
# .pop()
# Removes an item at a given index
best_elden_ring_weapons.pop(1)  #Remove Moonveil from the game

# .remove()
# Removes an item by value- removes the first instance of the value
best_elden_ring_weapons.remove("Blasphemous Blade") #If the value exist, it errors :(

# .append()
# Adds the value as a new item to the end of the list
best_elden_ring_weapons.append("Death's Poker")


numbers = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), ]
print(numbers)

# .sort()
# Sorts the numbers from smallest to greatest
numbers.sort()
print(numbers)

# max()
#Prints the largest number in the list!
print(max(numbers))

# min()
#Prints the smallest number in the list!
print(min(numbers))

#Strings.... are just... lists of characters :O
print(len("Osowski"))
'''
fav_food = ["Cheeeseburger", "Tacos", "Spaghetti"]
fav_candy = ("Sour Patch Kids", "Swedish Fish", "Twix")
cool_drugs =  []

print(fav_food[2])