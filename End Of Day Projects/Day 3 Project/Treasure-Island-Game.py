print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


#Write your code below this line 👇


advance = False
while advance == False:
  choice1 = input("You step off the boat and in front of you there are two options. The Temple of Enlightenment on the left and The Cave of Shadows on the right, which do you enter? \n Type 'Left' for temple or 'Right' for cave\n")
  choice_lowercase = choice1.lower()
  if choice_lowercase == "right":
    print("You have chosen to venture into The Cave of Shadows...")
    advance = True
  elif choice_lowercase == "left":
    print("You venture deeper into the temple and you find yourself enveloped in an unsettling aura. You stumble upon a concealed chamber with a hidden chest. You accidentally step on a pressure plate and the ceiling crushes you.")
    print("You Died Try Again.")
  else: 
    print("This was not one of the choices, try again")
advance = False
while advance == False:
  choice2_uppercase = input("As you continue into the cave you see a small illuminating lantern. You see 2 paths in front of you. The path on the right sounds like you hear water, the path on the left sounds like you hear a breeze. Which do you choose left or right?\n")
  choice2 = choice2_uppercase.lower()
  if choice2 == "left":
    print("You chose the left path, your foot slips and you fall off the cliff to your death.")
    print("You Died Try Again.")
  elif choice2 == "right":
    print("You follow the sounds of running water. After walking for 2 hours and 45 minutes, a sacred pool is revealed")
    advance = True
  else:
    print("This was not one of the choices, try again")
advance = False
while advance == False:
  choice3 = input("In the center of the sacred pool there is a small island with 2 pedestals. You swim across to get a closer look. One pedestals has a green gem and the other has a purple gem. Which do you grab, green or purple?\n")
  choice3_uppercase = choice3.lower()
  if choice3_uppercase == "green":
    print("You pick up the green gem. You hear splashes, turn around and a shark flys towards you out of the water. You cant react in time and it bits you in half. You Die. ")
    print("You Died Try Again.")
  elif choice3_uppercase == "purple":
    print("You pick up the purple gem and it starts to glow! The gem then starts talking to you and says 'Walk forward and the exit will be on your left'.")
    advance = True
  else: 
    print("This was not one of the choices, try again")
advance = False
while advance == False:
  choice4 = input("As you walk to the left, you see a large door. It says 'If you can answer this question you may leave this cafe unharmed.' He proceeds to ask 'What color is an orange?'\n")
  choice4_uppercase = choice4.lower()

  if choice4_uppercase == "orange":
    print("The door opens and you can see light pouring into the cave. You walk towards the light and suddenly you find yourself outside, next to the entrance where you went in. You are relieved to have escaped unscathed, and with some treasures in your hands. You then make your way back towards the boat to return home. \n")
    print("YOU WIN!")
    advance = True
  else:
    print("That was the incorrect answer")
    print("Try Again.")
  

