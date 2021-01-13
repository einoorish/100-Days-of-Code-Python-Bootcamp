import art
import game_data
import random
from replit import clear

def compareFollowerCount(index1, index2):
  '''
  Returns index of a person who has more followers
  '''
  
  followers1 = game_data.data[index1]["follower_count"]
  followers2 = game_data.data[index2]["follower_count"]

  if(followers1 > followers2):
    return index1
  else: return index2

def getPersonInfo(index):
  person = game_data.data[index]

  return (f"{person['name']}, a {person['description']}, from {person['country']}.")

def getAnswer(index1, index2):
  if(compareFollowerCount(index1, index2) == index1):
    return "A"
  else: return "B"


def startGame() :
  score = 0
  list_size = len(game_data.data)

  while(True):
    print(art.logo)

    if(score!=0):
      #previous answer was correct
      print(f"Correct! Your score is {score}")

    index1 = random.randint(0, list_size-1)
    index2 = random.randint(0, list_size-1)

    print("Compare A: " + getPersonInfo(index1))
    print(art.vs)
    print("Against B: " + getPersonInfo(index2))

    user_answer = input("Who has more followers? Type 'A' or 'B': ")

    clear()

    if(getAnswer(index1, index2) == user_answer):
      score+=1
    else: 
      print(f"Sorry, that was wrong. Final score is {score}")
      return




startGame()