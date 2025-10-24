def start_game():
    print("welcome to the text adventure game")
    inside()

    if __name__ == "__main__":
        start_game()

def look_inside():
    hat_present = "Hat"
    backpack_present = "Backpack"

    print("\nYou look around your room. You see:")
    print("1." + hat_present)
    print("2." + backpack_present)

    choice = input(">> ")
    
    
    if choice == "1":
        print("You found your hat! You probably should put it on.")
        look_inside()
    elif choice == "2":
        print("You open your backpack. Inside, you find:")
        print(inside_backpack())
        look_inside
    else:
        print("Invail choice. Try again.")
        look_inside()



def inside():
    print("You are in side your house. Do you:")
    print("1. Grab you hat and backpack")
    print("2. Sit at your desk")
    print("3. You look around in your room")

    choice = input(">> ")

    if choice == "1":
       Grab_Things()
    elif choice == "2":
        sit_down()
    elif choice == "3":
        inside_room()
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
    print("She wants you to go get your father. Do you:")
    print("1. Ingnore her")
    print("2. Do what she asks")
    print("3. Complain to her about not going to get dad")

    choice = input(">> ")

    if choice == "1":
        print("Son did you hear me?")
    elif choice == "2":
        print("Thank you son")
    elif choice == "3":
        print("Do now")
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
        enter_house()
    elif choice == "3":
        move_forward()
    else:
        print("Invalid choice and please try again.")
        outside()



def look_around():
    print("You look around and see:")
    print("1. Trees")
    print("2. Long Grass and bushes")
    print("3. You see dad")
    print("4. Head to the path")

    choose = input(">>> ")

    if choose == "1":
        print(" You see trees around you")
    elif choose == "1":
        print("You see long grasses and bushes around your house")
    elif choose == "3":
        print("You go looking for dad and you see him chopping a tree in the woods")
        print("After seeing dad you go up to him and bug him")
        print("You tell him that mom needs you badly")
        enter_house()
    elif choose == "4":
        move_forward(__path__)


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
        outside()
    else:
        print("Mistake... Cannot go there")
        enter_house()

    

def move_forward():
    print("You venture forward into the land, are you ready for you adventure")
    print("Do you have ")