'''
1. **Fortune Teller Setup**
    
    Introduce the fortune teller, who will ask for different numbers to provide mystical insights.
    
2. **Input Prompts with Type Requirements**
    
    The fortune teller asks for the user to input numbers to tell the fortune. You can ask any questions you want for this, but here are some examples:
    
    - Ask for the player’s **lucky number** (expects an integer).
    - Ask how many **years into the future** they want to see (expects a float).
    - Ask for a **magical multiplier** (expects a float).
3. **Error Handling Using try and except**
    
    Use try and except to:
    
    - Catch errors if the player inputs the wrong type.
    - Restart the function when an error occurs
4. Read out the fortune
    
    Take the input numbers and a random number to calculate the fortune.

'''

import random
fortune =  [
     "A new opportunity is on the horizon. Take a leap of faith!",
    "Your hard work will pay off sooner than you think.",
    "Be wary of a tall stranger. All is not as it seems.",
    "Unexpected good news is coming your way.",
    "The answer you seek lies within yourself.",
    "You will embark on an exciting journey in the coming year.",
]
def get_user_numbers():
     print("\n🔮 Welcome, traveler. I am the Great Pythoni.🔮")
     print("To peer into your future, I require some numbers from you.")

try:
     # Prompt for an integer input
        lucky_number = int(input("What is your lucky number? "))
        
        # Prompt for a float input
        years_ahead = float(input("How many years into the future do you wish to see? "))
        
        # Prompt for another float input
        multiplier = float(input("What is your magical multiplier? "))
        
        # Calculate the fortune
        # The random number is a float between 0.0 and 1.0, to add more variation
        random_factor = random.uniform(0.1, 1.0)
        fortune_index = int((lucky_number + years_ahead + multiplier + random_factor) % len(fortune))
        
        # Read out the fortune
        print("\n✨ The stars are aligning... ✨")
        print(f"Your fortune for the next {years_ahead} years is...")
        print(f"\n**{fortune[fortune_index]}**")
        
except ValueError:
        # This block catches errors if the user inputs text instead of a number
        print("\n🚫 That is not a number! The spirits are displeased. Let's try again. 🚫")
        get_user_numbers() # Recursively call the function to restart

get_user_numbers()
