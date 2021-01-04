import random

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

options = [rock, paper, scissors]

computer_choice = options[random.randint(0,2)]
player_choice = options[int(input("Choose 0 - rock, 1 - paper or 2 - scissors: "))]

print("Computer chose " + computer_choice)
print("You chose " + player_choice)

if computer_choice == player_choice :
  print("It's a draw!")
else:
  if player_choice == options[0] :
    if computer_choice == options[1]:
      print("You lose")
    else: print("You win")
  elif player_choice == options[1] :
    if computer_choice == options[2] :
      print("You lose")
    else: print("You win")
  elif player_choice == options[2] :
    if computer_choice == options[0]:
      print("You lose")
    else: print("You win")
  else :
    print("Wrong input")
