def JoeMoma():
    print("Yeah, this is self explanatory, don't expect this game to not pull random crap out of their butt. YOu have Options to make ")
    print("1. Go to Town")
    print("2. Go to the Forest.")
    choice = input(">")
    if choice == "1":
        GoTown()
    elif choice == "2":
        GoForest()
    else:
        print("Try Again!")
        JoeMoma()
def GoTown():
    print("You see blood every where")
    print("1. Find the person who caused this.")
    print("2. Steal Items so you can have something to defend yourself.")
    Scene1 = input(">")
    if Scene1 == "1":
        Killed()
    elif Scene1 == "2":
        Stolen()
    else:
        print("Uhhh why?")
    GoTown()
def Killed():
    print("Yeah, You Died")
    return("Bad Ending Acheived!")
def Stolen():
    print("You Stole Some stuff! YOU HAVE MORE OPTIONS")
    print("1. Fight the Monster")
    print("2. Skip to the ending")
    print("3. Escape to somewhere else")
    Scene2 = input(">")
    if Scene2 == "1":
        NeutralEnding()
    else:
        print("Error!")
    
    if Scene2 == "2":
        TheVoidEnding()
    elif Scene2 == "4":
        LocatedLake()
    else:
        print("error")
        Stolen()
    
def GoForest():
    print("You walked into the forest, there are 2 routes.")
    Fowoest = input(">")
    if Fowoest == "1":
        Meadow()
    elif Fowoest == "2":
        TheDarkForest()
        
def NeutralEnding():
    print("You're fighting a monster.")
    print("1. Attack the monster with your strength.")
    print("2. Outsmart the DreamMonster")
    Monster = input(">")
    if Monster == "1":
        Neutrality()
    elif Monster == "2":
        ItsADreamEnding()
def Neutrality():
    print("You Killed the Monster but you're alone with no one alive...")
    return("Neutral ending acheived!")
    #Neutral Ending Acheived!
def ItsADreamEnding():
    print("It's All fake?????")
    return("You got the dream ending!")
    #Yeah It's the Dream ending
def LocatedLake():
    print(" You ran to the Lake..")
    print("1. Explore The Area.")
    print("2.Escape the area so you won't be in danger")
    Lake = input(">")
    if Lake == "1":
        Exploration()
    elif Lake == "2":
        Escape()
    else:
        return("Error!")
def Exploration():
    print("You Found a Secret Potion!")
    print("1. Fight the Monster Now")
    print("2. Drink the potion.")
    print("3. *Gets Transported to somewhere else.* ")
    Explore = input(">")
    if Explore == "1":
        CoolEnding()
    elif Explore == "2":
        RealityEnding()
    else:
        return("Error!")
    if Explore == "3":
        GensokyoEnding()
    else:
        return("Error!")
def CoolEnding():
    print("Nice you won against them by poisoning the monster without any help!")
    #They Used a potion against them
def RealityEnding():
    print("You drank the potion and found yourself in front of your own house. you're in your actual world")
    #This is different from the 'Dream ending' as in the person is trapped in the world vs the person dreaming about it
    return("Reality ending acheived!")
def GensokyoEnding():
    print("You touched the potion and find your self at the Fantasy land. You see a shrine named 'The Hakurei Shine'")
    #This is similar to the Reality ending except it's real and They're being transported to Gensokyo after touching the potion
    return("You got the Gensokyo Ending!")
def TheVoidEnding():
    print("You skipped to the ending but this one is unfinished.")
    return("Void Ending! Try again!")

def Meadow():
    print("You feel wonderful, but it's TOO wonderful to be here")
    print("1. You stay in the Meadow a little bit longer...")
    print("2. Escape The Meadow into the Abandoned city.")
    ChoicesGoHere = input(">")
    if ChoicesGoHere == "1":
        Insanity()
    elif ChoicesGoHere == "2":
        AbandonedCity()
    else:
        return("Error!")
def Insanity():
    print("You start to go insane in this place...")
    print("1. Still stay here.")
    print("2. Walk through the path to get out.")
    Insane = input(">")
    if Insane == "1":
        InsaneEnding()
    elif Insane == "2":
        TheFancyCity()
    else:
        return("Error!")
def InsaneEnding():
    print("You went Insane due to the Stimulus here.")
    return("You got the Insane Ending!")
def TheDarkForest():
    print("You see a glowing substance in the distance.")
    print("1. Touch this substance")
    print("2. Avoid this substance Completely")
    TheForest = input(">")
    if TheForest == "1":
        Sickness()
    elif TheForest == "2":
        ACliffAhead()
    else:
        return("Error")
    
def Sickness():
    print("You touch the substance and got sick from it. You feel like a sense of impending doom.")
    print("1. Keep Going down the path.")

def TheFancyCity():
    print("You reached The Fancy City. You have a couple of option")
    print("1. Live in the city.")
    print("2. Walk on.")
    HeartfeltFancy = input(">")
    if HeartfeltFancy == "1":
        GreatEnding()
    elif HeartfeltFancy == "2":
        ThecaveWithin()
    else:
        return("Error!")
    TheFancyCity()
def GreatEnding():
    print("You live in the city. Now you're sucessful in businesses!")
    return("You got the Great Ending!")
def ThecaveWithin():
    print("You go out of the city and you walked into a cave and you went in there. There Are 4 paths to take.")
    print("1. Go to the Far left.")
    print("2. Go to the central right.")
    print("3. Go to far right.")
    print("4. Go to central left.")
    Caves = input(">")
    if Caves == "1":
        StuckEnding()
    elif Caves == "2":
        AttackedEnding()
    elif Caves == "3":
        LoadsOfMoney()
    elif Caves == "4":
        MadeItOut()
    else:
        print("Error!")
def StuckEnding():
    print("You went this route and fell and got stuck in a cave spot. Now you can't escape.")
    return("Stuck Ending acheived!")
def AttackedEnding():
    print("You were attacked by a Cave monster and tried to get out.")
    return("You got the Attacked ending!")
def LoadsOfMoney():
    print("You found money while taking this route.")
def Escape():
    print("How would you escape?")
    print("1. Build a Boat.")
    print("2. Run by foot.")
    Choices = input(">")
    if Choices == "1":
        BoatEnding()
    elif Choices == "2":
        FootEnding()
    else:
        return("Error!")
def BoatEnding():
    print("You escape by the boat and arrived at a land of mysterium")
    return("You got the boat ending!")
def FootEnding():
    print("You ran until you arrived at the land of the spider lillies.")
    return("You got the Foot ending!")
def AbandonedCity():
    print("You're at the Abandoned City and you don't know what you're doing. You have options.")
    print("1. Go explore the city.")
    print("2. Stay at the City.")
    City = input(">")
    if City == "1":
        FoodEnding()
    elif City == "2":
        PoorEnding()
    else:
        return("error")
    AbandonedCity()
def FoodEnding():
    print("You found food in one of the buildings")
    return("You got the food ending, so random!")
def PoorEnding():
    print("You are stuck at this city not knowing what to do or find!")
    return("You got the poor ending!")

def MadeItOut():
    print("You made out of the cave. You have a few options")
    print("1. Meet with Mr. Osowski")
    print("2. Find the Button")
    c00l = input(">")
    if c00l == "1":
        MrOsowskiEnding()
    elif c00l == "2":
        Buttonisation()
    else:
        return("Error!")
    MadeItOut()
    
def ACliffAhead():
    print("You found a cliff ahead, You also found a Bridge.")
    print("")
def MrOsowskiEnding():
    print("You found Mr. Osowski and he's the teacher of this student's game")
    return("You found the Mr. Osowski ending!")
def Buttonisation():
    print("You found a button and pressed it. You got transported into a kingdom; you have a few options.")
    print("1. Talk to the townspeople.")
    print("2. Go to the Castle")
    #This is different from the Town earlier where the people are alive instead of dead.
    Town = input(">")
    if Town == "1":
        MysteriousPerson()
    elif Town == "2":
        MeetKing()
    else:
        return("Error!")
    Buttonisation()
def MysteriousPerson():
    print("You Interacted with this person. They offer to teleport you.")
    print("1. Accept their offer")
    print("2. Refuse and stay in the town")
    Offering = input("")
    if Offering == "1":
        Athome()
    elif Offering == "2":
        MedievalEnding()
    else:
        return("Error!")
    MysteriousPerson()
def Athome():
    print("You're teleport to your house")
    return("House Ending Unlocked!")
def MeetKing():
    print("You meet with the king. You have options to make")
    print("1. Try to dethrone him.")
    print("2. Try to Assassinate him. ")
    King = input(">")
    if King == "1":
        KingEnding()
    elif King == "2":
        JailedEnding()
    else:
        return("Error!")
    MeetKing()
def MedievalEnding():
    print("Yeah you know what happend.")
    return("Medieval ending Unlocked!")
def KingEnding():
    print("You manage to overthrow him forcefully and fully took power of the kingdom, somehow.")
    return("King Ending!")
def JailedEnding():
    print("You tried to assassinate the king but you got thrown in to Jail for doing so.")
    #This is different from the Stuck ending as it takes in a different place and also you aren't falling.
    return("You got the Jailed ending!")






    





    






    



#Mr. osowski Making me want to cry on the floor 😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭