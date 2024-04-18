# prompt the user for of speech and then store them into variables.
# output the template on the screen with all the blanks fill out.

# Your character starts his/her mission from the start. Input plot intro accordingly.

# "Would you like to pick up the handgun __verb__?"

import time
import sys
game_title = "final fear"
game_title = game_title.upper()
print("Warning: This game contains scenes of explicit violence and gore. ")
print("....................................................................")
print("....................................................................")
print()
print("                    ''' Welcome to", game_title, "'''")
print()
print("....................................................................")
print("....................................................................")
print()
print()

def get_menu_options():
    menu_options = ('s', 'e', 'h')

    while True:
        user_input = input("Type 'S' to Start the game / 'E' to Exit / 'H' for Help: ")

        if user_input in menu_options:
          return user_input
    
        else:
             print("Invalid selection. Try again")
while True:
    user_input = get_menu_options()        
    if user_input == 's':
        print('Game loading...')
        time.sleep(5)
        break

    elif user_input == 'e':
        user_input = input("Do you wish to quit? (Type Y/N): ")
    if user_input <= 'y':
        print()
        sys.exit("You just left the game. Hope to see you again soon!\n ")
    if user_input == 'n':
        user_input = get_menu_options()
        print(game_title)
        continue
            
 


        

# if intro_menu == 'EXIT':
#     intro_menu = input("Do you wish to quit? (Type Y/N): ")
# if intro_menu == 'Y':
print()

# character dictionaries with key/value pairs 
# Keys and Values are wrapped in quotes, separated by colons
# key/value pairs are separated by commas
char1 = {"Name": "Jason Baker", "Skills": "Combat Specialist",
         "Power": "300", "Stamina": "180", "Weapon": "Heavy Machine Gun"}
char2 = {"Name": "Vicky Anderson", "Skills": "Paranormal Forensics",
         "Power": "160", "Stamina": "220", "Weapon": "Psychic Force"}
char3 = {"Name": "Satori Kageryu", "Skills": "Stealth Tactics",
         "Power": "210", "Stamina": "270", "Weapon": "Handguns & Katana Blade"}

decharacter_sel = (char1, char2, char3)
print("----------SELECT YOUR CHARACTER----------")

# single function to print any character stats


def charStats(character):
    for key, value in character.items():
        print(f'{key}: {value}')


# print each character stats
charStats(char1)
print()
charStats(char2)
print()
charStats(char2)
print()

# variable to store selected character
selected_character = None

# while loop to gather selected character input (1, 2 or 3)
while True:
    print("""
1) Jason Baker
2) Vicky Anderson
3) Satori Kageryu
""")
    # prompt for selection
    char_select = input("Choose your character by number: ")
    if char_select in "1" "2" "3":
        if char_select == "1":
            selected_character = char1
        elif char_select == "2":
            selected_character = char2
        elif char_select == "3":
            selected_character = char3
        # this is how you can access the values of a certain key in the selected_character
        # variable_name['key_name'] as seen on next line 
        print(f"You chose {selected_character['Name']}! \n")
        # break out of while loop
        break
    else:
        print('Invalid choice. Try again!')
        # restart while loop
        continue


# now selected_character will hold the dictionary they chose throughout rest of app 

print("Welcome to a new dimension of horror. Will you survive the night? ")
print(f"{selected_character['Name']}, you are an elite squad member working for a private investigation team named P.I.T.F.(Paranormal Investigation Task Force). ")
print("You've been assigned to investigate in the Crimson Mansion. A place that holds a sinister reputation, due to the amount of negative energy events (NEEs') that accumulated over the years. Lately, there have been several reports of people disappearing whenever they approach Crimson Mansion. In their place, comes something else. Something wicked that reeks of negative energy. We spotted 2 of those in our town last week. They seemed like normal human beings from afar, as we approached them, their shaped bented under the street light. They turned or the corrupted as we investigators call em'.")