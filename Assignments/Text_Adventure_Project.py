score = 0

def start_game():
    print("You are a 20 year old, living in the 1850s, and you still live with your parents.")
    print("But you are lazy and do not want to leave them so you deside to help them around the house.")
    print("But you decided either live with your parents forever or live a life wothout them.")
    print("welcome to the text adventure game")
    inside()

def look_inside():
    global score
    hat_present = "Hat"
    backpack_present = "Backpack"

    print("\nYou look around your room. You see:")
    print("1." + hat_present)
    print("2." + backpack_present)
    print("3. Your computer and phone at your desk")

    choice = input(">> ")
    
    if choice == "1":
        print("You found your hat! You probably should put it on.")
        score += 1
        Grab_Things()
    elif choice == "2":
        inside_backpack()
        look_inside()
    elif choice == "3":
        inside()
    else:
        print("Invail choice. Try again.")
        look_inside()

def inside_backpack():
    print("Inside of your backpack you have: ")
    print("1. Seeds")
    print("2. Food")
    print("3. Water")
    print("4. Lighter")
    print("5. Phone")
    print("6. Sleeping Bag")
    print("7. Tools")
    

    choice = (">> ")
    if choice in {"6", "7"}:
        look_inside()
    else:
        print(f"You grab an item number {choice}.")
        inside_backpack()

def inside():
    print("You are inside your house. Do you:")
    print("1. Grab you hat and backpack")
    print("2. Sit at your desk")
    print("3. You look around in your room")
    print("4. Go down stairs")

    choice = input(">> ")

    if choice == "1":
       Grab_Things()
    elif choice == "2":
        sit_down()
    elif choice == "3":
        look_inside()
    elif choice == "4":
        print("You go down stairs and sit on the couch")
    else:
        print("Invalid choice. Try again.")
        inside()

def Grab_Things():
    print("You grab your things and head down stairs.")
    print("Once down stairs. Do you: ")
    print("1. Help Mom")
    print("2. Go outside")
    print("3. You grab you phone on your desk near you")


    choice = input(">> ")
    if choice == "1":
        Help_Mom()
    elif choice == "2":
        outside()
    elif choice == "3":
        play_phone()
    else:
        print("Wrong Choice. Please Try Again.")
        Grab_Things()

def Help_Mom():
    global score
    print("She wants you to go get your father. Do you:")
    print("1. Ingnore her")
    print("2. Do what she asks")
    print("3. Complain to her about not going to get dad")

    

    choice = input(">> ")

    if choice == "1":
        score -= 1
        print("Son did you hear me?")
        Help_Mom()
    elif choice == "2":
        score += 2
        print("Thank you son")
    elif choice == "3":
        score -= 1
        print("Do now")
        Help_Mom()
    else:
        print("Try Again.")
        Help_Mom()

def play_phone():
    print("You sit down on the couch and you have a few options to pick from. Do you: ")
    print("1. Watch social media")
    print("2. Play Clash Royal")
    print("3. Play Clash of Clans")
    print("4. Bloons TD6")
    print("5. Play Brawl Stars")
    print("6. Fortnite")
    print("7. Go to the app store")
    print("8. Head upstairs play on phone if tired on you phone")
    print("9. Help mom")
       
    choice = input(">>> ")
   
    if choice == "1":
        print("You have entered the game")
    elif choice == "2":
        print("You have entered the game")
    elif choice == "3":
        print("You have entered the game")
    elif choice == "4":
        print("You have entered the game")
    elif choice == "5":
        print("You have entered the game")
    elif choice == "6":
        print("You have entered the game")
    elif choice == "7":
        print("You have entered the appstore")
    elif choice == "8":
        print("Head upstairs")
        hook_phone()
    elif choice == "9":
        Help_Mom()
    else:
        print("Invalid choice and please try again.")
        play_phone()

def hook_phone():
    print("You hook your phone to the computer to play game. What game do you choose: ")
    print("1. Play Clash Royal")
    print("2. Play Clash of Clans")
    print("3. Bloons TD6")
    print("4. Play Brawl Stars")
    print("5. Fortnite")
    print("6. Minecraft")
    print("7. Grab your things")

    choice = input(">> ")

    if choice == "1":
        print("You have entered Clash Royal")
    elif choice == "2":
        print("You have entered Clash of Clans")
    elif choice == "3":
        print("You have entered Bloons TD6")
    elif choice == "4":
        print("You have entered Brawl Stars")
    elif choice == "5":
        print("You have entered Fortnite")
    elif choice == "6":
        print("You have entered Minecraft")
    elif choice == "7":
        Grab_Things()
    else:
        print("You Failed pls try again.")
        hook_phone()

def sit_down():
    print("You sit down at your desk and play video game.")
    print("After sitting down to play video games. Waht game do you play: ")
    print("1. Minecraft")
    print("2. Pull out phone and hook up to computer.")
    print("3. Fortnite")
    print("4. Go search for steam and download")
    print("5. Play Call Of Duty")
    print("6. Roblox")
    print("7. Get up, had grabed your things, and went outside")
    
    choice = input(">>> ")
   
    if choice == "1":
        print("You have entered Minecraft")
    elif choice == "2":
        hook_phone()
    elif choice == "3":
        print(" You have entered Fortnite")
    elif choice == "4":
        print(" You have downloaded steam and now entering")
    elif choice == "5":
        print("You have entered Call of Duty")
    elif choice == "6":
        print(" You have entered roblox")
    elif choice == "7":
        Grab_Things()
    else:
        print("Invalid choice and please try again.")
        sit_down()

def outside():
    print(" You stand at the front door of your house. Do you:")
    print("1. Look around")
    print("2. Enter house")
    print("3. Go forward to adventure the land")
    
    choice = input(">>> ")
   
    if choice == "1":
        look_around()
    elif choice == "2":
        score += 1
        enter_house()
    elif choice == "3":
        score += 1
        move_forward()
    else:
        print("Invalid choice and please try again.")
        outside()

def look_around():
    score += 2
    print("You look around and see:")
    print("1. Trees")
    print("2. Long Grass and bushes")
    print("3. You see dad")
    print("4. Head to the path")

    choose = input(">>> ")

    if choose == "1":
        print(" You see trees around you")
    elif choose == "2":
        print("You see long grasses and bushes around your house")
    elif choose == "3":
        score += 2
        print("You go looking for dad and you see him chopping a tree in the woods")
        print("After seeing dad you go up to him and bug him")
        print("You tell him that mom needs you badly")
        enter_house()
    elif choose == "4":
        move_forward()

def enter_house():
    print("You enter the house from coming outside")
    print("Now you do not know what to do next. But think on what do you want to do?")
    print("1. Sit on the couch and play your phone")
    print("2. You can sit on you chair in you room, play video game, and stream at the same time")
    print("3. Head back outside")


    choose = input(">>> ")

    if choose == "1":
        play_phone()
    elif choose == "2":
        sit_down()
    elif choose == "3":
        score += 4
        outside()
    else:
        print("Mistake... Cannot go there")
        enter_house()

def move_forward():
    print("You venture forward into the land, are you ready for you adventure")
    print("want to look at things before you go: ")
    print("1. Look inside of backpack")
    print("2. Make sure computer was off")
    print("3. See where a pitch fork in the road is on your jouney")


    choice = input(">>> ")

    if choice == "1":
        check_backpack()
    elif choice == "2":
        print("Look inside of your bedroom")
        inside()
    elif choice == "3":
        print("You pull out your phone and you decide to look up where the pitch in the road is up ahead of you.")
    else:
        print("You failed")
        move_forward()

def start_adventure():
    print("After checking for your things. You decide to move forward along the path.")
    print("You come a across a fork in the road. Do you go left or right")
    print("1. Right")
    print("2. Left")

    global score 

    choice = (">>> ")

    if choice == "1":
        score += 1
        right_1()
    elif choice == "2":
        score += 1
        left_1()
    else:
        print("Try Again")
        start_adventure()

def right_1():
    print("You go over a bridge. You come to a another fork in the road and it has three paths. Do you:  ")
    print("1. Right")
    print("2. Left")
    print("3. Center")

    choice = (">>>")

    if choice == "1":
        score += 1
        right_2()
    elif choice == "2":
        score += 1
        left_2()
        game_over()
    elif choice == "3":
        score += 1
        center()
    else:
        print("You failed. Try again")
        right_1()
    
def left_1():
    print("You go into a town")
    score += 1
    print(f"Your score in total {score}")
    game_over()

def right_2():
    print("You go into another town far far away. From your parnet it has been 31 day since you have left")
    score += 1
    print(f"Your score in total {score}")
    game_over()

def left_2():
    score += 1
    print(f"Your score in total {score}")
    game_over()

def center():
    print("You you move forward into a fork in the road")
    print("1. Right")
    print("2. Left")

    choice = (">>> ")

    if chioce == "1":
        score += 1
        right_3()
    elif choice == "2":
        score += 1
        left_3()
    else:
        print("You Failed.")
        
def Right_3():
    score += 1
    print(f"Your score in total {score}")
    game_over()

def check_backpack():
    num = num
    Seeds = input("How many different seeds do you have?\n> ")
    Food = input("How much food do you have?\n> ")
    Water = input("How many jugs of water do you have?\n> ")
    Phone = input("What is your phone battery percent?\n> ")
    print("Check Supplies")
    print("Seeds: " + Seeds)
    print("Food: " + Food)
    print("Water Jugs: " + Water)
    print("Battery Percent: " + Phone)

    if int(Seeds) >= 5 and int(Food) >= 5 and int(Water) >= 3 and int(Phone) >= 50:
        print("You have enough supplies to continue your adventure.")
        start_adventure()
    else:
        print("You do not have enough supplies to continue your adventure. You head back home to get more supplies.")
        start_adventure()

def check_final_score_range():
    global score
    target = 15
    tolerance = 2
    
    # Calculate the minimum and maximum acceptable scores
    min_score = target - tolerance # 8
    max_score = target + tolerance # 12
    
    print(f"\nChecking if score is within the acceptable range: {target} \u00B1 {tolerance}")
    print(f"Your current score is: {score}")

    # The if statement checks if the score is greater than or equal to the minimum
    # AND less than or equal to the maximum.
    if score >= min_score and score <= max_score:
        print("Success! Your score is within the golden range.")
        print(f" (Between {min_score} and {max_score})")
    else:
        print("Failure. Your score is outside the required range.")

def game_over():
    global score
    print("\n" + "="*4)
    print(f"GAME OVER! Your final score is: {score}")
    
    check_final_score_range

    if score <= 2:
        print("When you see your dad and help your mother out. You choose to stay with them until there death and live there until you die as well.")
    elif score == 3:
        print("If you go left you move to a city near by your family and live there and find someone and marry them and have kid to pass on your genes.")
    elif score == 4:
        print("if you choose to do right you move over a bridge and go right again. You go to a far town away and you never see your parnets but fall in love with someone else you meet in that town or city.")
    elif score == 5:
        print("if you went right and the hit another pitch fork in the road. You go strait on the road you live by your self on a country road.")
    elif score == 6:
        print("if you went right and the hit another pitch fork in the road and go strait on the road you live by your self on a country road.")
    elif score >= 10:
        print("(Secret Ending) If you went lef into a towm and keep on going you wnet into a forest. In the forest you get mauled by a bear and when word gets to your parents you have die. They die because of your passing")
    else:
        print("You have a unique ending that is not listed.")
    
    print("Thanks for playing!")
    print("="*4)

if __name__ == "__main__":
    start_game()