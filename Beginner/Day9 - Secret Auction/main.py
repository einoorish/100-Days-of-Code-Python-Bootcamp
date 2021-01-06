from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)

all_bids = {}

def find_the_winner() : 
  highest_bid = 0
  winner = ""

  for name in all_bids : 
    if all_bids[name] > highest_bid :
      highest_bid = all_bids[name]
      winner = name

  print(f"The winner is {winner} with a bid of ${highest_bid}")

    
def add_new_person() :
  name = input("Enter your name: ")
  bid = int(input("Enter your bid: "))
  all_bids[name] = bid



should_continue = True

while(should_continue): 

  add_new_person()

  add_another = input("Is there another person who wants to make a bid? [yes/no]\n")

  if add_another == "yes":
    clear()
  else: 
    should_continue = False
    find_the_winner()

  
  