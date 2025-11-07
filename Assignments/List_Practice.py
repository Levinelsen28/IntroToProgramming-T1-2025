fav_fruit = ["Apple", "Banana", "Pineapple",  "Grapes", "Pickle"]
print(fav_fruit[0])
print(fav_fruit[-1])

fav_fruit.append(input("give me another fruit\n>"))

fav_fruit.pop(input("Which fruit do you not like?\n>"))

fav_fruit.sort()
print(fav_fruit)