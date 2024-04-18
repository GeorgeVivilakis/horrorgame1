# prompt the user for of speech and then store them into variables.
# output the template on the screen with all the blanks fill out.

# Your character starts his/her mission from the start. Input plot intro accordingly.

# "Would you like to pick up the handgun __verb__?"

import sys
game_title = "final fear"
game_title = game_title.upper()
print("Warning: This game contains scenes of explicit violence and gore. ")
print("....................................................................")
print("....................................................................")
print()
print("                    ''' Welcome to", game_title,"'''")
print()
print("....................................................................")
print("....................................................................")
print()
print()
intro_menu = input("Type 'ENTER' to start game or 'EXIT' to quit: ")
while intro_menu != 'ENTER':
    if intro_menu == 'ENTER':
         continue
    if intro_menu == 'EXIT':
         intro_menu = input("Do you wish to quit? (Type Y/N): ")
    if intro_menu == 'Y':
         print()
         sys.exit("You just left the game. Hope to see you again soon!\n ")
    if intro_menu == 'N':
         print("Do you wish start the game?") 
    else:
          intro_menu = input("Invalid selection. Type ENTER to start the game or EXIT to quit: ")
          print()

# character dictionaries with key/value pairs 
# Keys and Values are wrapped in quotes, separated by colons
# key/value pairs are separated by commas

character1 = {'Name': 'Jason Baker', 'Skills': 'Combat Specialist', 
              'Power': '300', 'Stamina': '180', 'Weapon': 'Heavy Machine Gun' }
character2 = {'Name': 'Vicky Anderson', 'Skills': 'Paranormal Forensics',
              'Power': '160', 'Stamina': '220', 'Weapon': 'Psychic Force'}
character3 = {'Name': 'Hayate Kimura', 'Skills': 'Stealth Tactics',
              'Power': '!60', 'Stamina': '270', 'Weapon': 'Handguns & Swords'}


print("----------SELECT YOUR CHARACTER----------")

# single function to print any character stats

def char_stats(character):
     for key,value in character.items():
          print(f'{key}: {value}')

# print each character stats
char_stats(character1)
print()
char_stats(character2)
char_stats(character3)

# variable to store selected character
selected_character = None

# while loop to gather selected character input (1, 2 or 3)
while True:
     print("""
1) Jason Baker
2) Vicky Anderson
3) Hayate Kimura
""")
     input_select = input('Select your character by number as indicated below: ')
     if input_select in '1' '2' '3':
          if input_select == '1':
               selected_character = character1
          elif input_select == '2':
               selected_character = character2
          elif input_select == '3':
               selected_character = character3
        # this is how you can access the values of a certain key in the selected_character
        # variable_name['key_name'] as seen on next line 
          print(f"You have chosen {selected_character['Name']}! \n")
          break
          #break out of while loop
     else:
          print('Invalid choice. Try again!')
         #restart loop
          continue
    
print("Welcome to a new dimension of horror. Will you survive the night? ")
print("---------------------------------------------------------------------------------------------")
print(f"{selected_character['Name']}, you are an elite squad member working for a private investigation team named P.I.T.F.(Paranormal Investigation Task Force). ")
print("You've been assigned to investigate in the Crimson Mansion. A place that holds a sinister reputation, due to the amount of negative energy events (NEEs') that accumulated over the years. ") 
print("Lately, there have been several reports of people disappearing whenever they approach Crimson Mansion. In their place, comes something else. Something wicked that reeks of negative energy. ") 
print("We spotted 2 of those in our town last week. They seemed like normal human beings from afar, as we approached them, their shaped bented under the street light. They turned or the corrupted as we investigators call em'.")
print()
