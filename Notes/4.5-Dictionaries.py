'''
# Dictionary is a type of collection like a list
# A list is a colelciton of items in a sequence
# A Dictionary is different
# Dictionaries store data in key-value pairs
# You can retreive data quickly by using a unique key
# instead of retreving it by index (position)

#Example
# Lists use brackets, dictionaries use braces
osowski = {
    "name": "Osowski",
    "age": 31,
    "city": "St. Michael",
    "pets": 2,
    "height": 5.8
}
# Each key must be unique

# Retreiving values from a dictionary

print(osowski["age"])

# .get allows you to retreive a value without erroring
# when the key doesn't exist
# The second parameter is what is given if value is not found
print(osowski.get("height"))
print(osowski.get("weight", "fortnite"))

# You can add values to a dictionary
osowski["country"] = "USA"

# You can modify values
osowski["age"] = 32

print(osowski)

# Remove entries
osowski.pop("pets")

# Iterate through a dictionary using a for loop
for key, value in osowski.items():
    print(key + ": " + str(value))

# Dictionary functions
print(osowski.keys())   #returns all keys
print(osowski.values()) #returns all values
print(osowski.items())  #returns all pairs
print(osowski.clear())  #removes all items from the dict
'''

