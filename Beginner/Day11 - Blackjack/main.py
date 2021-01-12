############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import art
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []

player_sum = 0
dealer_sum = 0

def addRandomCard(deck) :
  card = random.choice(cards)
  deck.append(card)
  return card

def sumCards(deck) :
  sum = 0
  for card in deck:
    sum+=card
    
  return sum

def compare():
  if(player_sum == dealer_sum):
    print("It's a Draw.")
  elif player_sum > dealer_sum:
    print("You win!")
  else:
    print("You lose.")
    
def printResults():
  print(f"   Your final hand: {player_cards}, final score: {player_sum}")
  print(f"   Computer's final hand: {dealer_cards}, final score: {dealer_sum}")  

def gameOver() :
  dealer_sum = sumCards(dealer_cards)
  if(dealer_sum == 21) : 
    # If computer gets blackjack, then the user loses (even if the user also has a blackjack).
    print("You lose.")
    return True

  player_sum = sumCards(player_cards)
  if(player_sum == 21) : 
    # If the user gets a blackjack, then they win
    print("You won!")
    return True
  elif(player_sum > 21) : 
    if 11 in player_cards :
      #If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.  
      player_cards[player_cards.index(11)] = 1
      player_sum-=10

      if(player_sum > 21) :
        #But if player sum is still over 21, they lose
        print("You lose.")
        return True
      elif(player_sum == 21):
        print("You win.")
        return True

  #Since neither has a blackjack and player sum is less than 21, continue the game
  return False
      
def game():
  global player_sum
  global dealer_sum
  #Deal both user and computer a starting hand of 2 random card values.
  for i in range(0,2):
    addRandomCard(player_cards)
    addRandomCard(dealer_cards)

  if(not gameOver()):
    player_sum = sumCards(player_cards)
    dealer_sum = sumCards(dealer_cards)

    print(f"Your cards: {player_cards}, current score: {player_sum}")
    print(f"Computer's first card: {dealer_cards[0]}")

    while(input("Type 'y' to get another card, type 'n' to pass: ") == "y"):
      player_sum += addRandomCard(player_cards)
      print(f"Your cards: {player_cards}, current score: {player_sum}")

      if(not gameOver()):
        #Computer's turn. The computer should keep drawing cards unless their score goes over 16.
        dealer_sum = sumCards(dealer_cards)
        if(dealer_sum < 17):
          dealer_sum += addRandomCard(dealer_cards)
          if(dealer_sum > 21) :
            print("You win!")    
            printResults() 
            return

  #Compare user score with computer score to see if userscore is higher     
  printResults()  
  compare()

def startGame() :
  while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    #clear data: 
    player_cards.clear()
    dealer_cards.clear()
    #clear screen
    clear()
    #play game
    print(art.logo)
    game()





startGame()
