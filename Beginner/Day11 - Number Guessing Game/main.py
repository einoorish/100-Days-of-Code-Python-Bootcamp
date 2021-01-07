from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def setDifficulty() :
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty=="easy" : 
    return EASY_LEVEL_TURNS
  elif difficulty=="hard" : 
    return HARD_LEVEL_TURNS
  else : print("Wrong input")

def check_answer(answer, guess, turns_left) :
  if answer == guess :
    return True
  else:
    if guess < answer :
      print("Too low.")
    else: 
      print("Too high.")
    turns_left-=1
    print(f"Turns left: {turns_left}")

def start_game() :
  turns_left = setDifficulty()

  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)

  guess = 0
  while turns_left>0 :
    guess = int(input("Make a guess: "))
    if check_answer(answer, guess, turns_left) :
      break
    else:
      turns_left-=1

  if turns_left == 0:
      print(f"You lost. The correct answer was {answer}")
  else:
      print(f"You won! The answer is {answer}")


start_game()
