rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
plays_string = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n")

plays = ["rock", "paper", "scissors"]

length_plays = len(plays)

a = 0
b = length_plays
computer_generated = random.randrange(a, b)

#If the user plays rock
if int(plays_string) == 0 and int(computer_generated) == 0:
  print(f"You chose \n{rock}\nComputer chose:\n{rock}\n Its a tie")
if int(plays_string) == 0 and int(computer_generated) == 1:
  print(f"You chose \n{rock}\nComputer chose:\n{paper}\n You Lose")
if int(plays_string) == 0 and int(computer_generated) == 2:
  print(f"You chose \n{rock}\nComputer chose:\n{scissors}\n You Win")
  
#If the user plays paper
if int(plays_string) == 1 and int(computer_generated) == 0:
  print(f"You chose \n{paper}\nComputer chose:\n{rock}\n You Win")
if int(plays_string) == 1 and int(computer_generated) == 1:
  print(f"You chose \n{paper}\nComputer chose:\n{paper}\n Its a tie")
if int(plays_string) == 1 and int(computer_generated) == 2:
  print(f"You chose \n{paper}\nComputer chose:\n{scissors}\n You Lose")
  
#If the user plays scissors
if int(plays_string) == 2 and int(computer_generated) == 0:
  print(f"You chose \n{scissors}\nComputer chose:\n{rock}\n You Lose")
if int(plays_string) == 2 and int(computer_generated) == 1:
  print(f"You chose \n{scissors}\nComputer chose:\n{paper}\n You Win")
if int(plays_string) == 2 and int(computer_generated) == 2:
  print(f"You chose \n{scissors}\nComputer chose:\n{scissors}\n Its a tie")
