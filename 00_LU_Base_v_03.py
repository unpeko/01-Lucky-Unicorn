import random 

# Functions go here...

def yes_no(question) :
  valid = False
  while not valid:
    response = input(question).lower()

    if response == "yes" or response == "y":
      response = "yes"
      return response

    elif response == "no" or response == "n":
      response = "no"
      return response

    else: 
        print("Please answer yes / no")


def instructions():
    print()
    statement_generator("Instruction Manual", "0")
    print()
    print(" Introduction ")
    print("This is a simple online slot machine game. The game is started by pressing 'Enter' and is exited by inputting 'XXX'. The goal is to match symbols on the spin to win. No real money is involved; this is a mock project for educational purposes. ")
    print()
    print(" Game Rules ")
    print()
    print(" Starting the Game. ")
    print("To start the game, simply press the 'Enter' key on your keyboard. ")
    
    print("Spinning the Reels: Once the game starts, the reels will spin automatically. In a traditional slot machine game, there would be multiple reels (usually three or five) each with a variety of symbols.")
    
    print("Outcome: After the reels stop spinning, your screen will display a variety of symbols on each reel. The aim is to match symbols across the reels according to the game's paylines. A payline is a line that spans the reels, and getting the same symbol on a payline across all reels usually results in a win.")
    
    print("Scoring: The game might have its own scoring system, for example, matching three of the same symbols might give you a certain number of points, four matching symbols might give more points, and so on.")
    
    print("Winning the Game: The objective is to accumulate as many points as possible by matching symbols on the reels.")
    
    print("Exiting the Game: To exit the game at any point, type 'XXX' in the game window. This will close the game. ")
    print()
    return ""


def num_check(question, low, high):
  error = "Please enter an whole number between 1 and 10\n"
  
  valid = False
  while not valid:
      try:
        #ask the question
        response = int(input(question))
        # if the amount is too low / too high give 
        if low < response <= high:
          return response 
    
        # output an error 
        else:
            print(error)
  
      except ValueError:
        print(error)    


def statement_generator(statement, decoration) :

  sides = decoration * 3 

  statement = "{} {} {}".format(sides, statement, sides)
  top_bottom = decoration * len(statement)

  print(top_bottom)
  print(statement)
  print(top_bottom)

  return ""


# Main routine goes here...

statement_generator("welcome to the lucky unicorn game", "*")
print()

played_before = yes_no("Have you played the game before? ")

if played_before == "no":
  instructions()

print()
statement_generator("lets get started","-")
print()

# Ask user how much they want to play with...
how_much = num_check("How much would you "
                    "like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

  # increase # of rounds played
  rounds_played += 1

  # print round number
  print()
  print(" Round #{} ".format(rounds_played))
  decoration = "1"

  chosen_num = random.randint(1, 100)

  # adjust balance 
  # If the random # is between 1 and  5,
  # user gets a unicorn (add $4 to balance)
  if 1 <= chosen_num <= 5:
    chosen = "unicorn"
    decoration = "2"
    balance += 4

  # if the random # is between 6 and 36 
  # user gets a donkey (subtract $1 from balance)
  elif 6 <= chosen_num <= 36:
    chosen = "donkey"
    decoration = "1"
    balance -= 1

  # the token is ether a horse or a zebra...
  # in both cases, subtract $0.50 from the balance 
  else:
    # if the number is even, set the chosen 
    # item to horse 
    if chosen_num % 2 == 0:
      chosen = "horse"
      decoration = "0"

    #otherwise set it to a zebra 
    else: 
      chosen = "zebra"
      decoration = "z"
    balance -= 0.5

  outcome = "You got a {}.  Your balance is " \
       "${:.2f}".format(chosen, balance)
  statement_generator(outcome, decoration)

  if balance < 1:
    # If balance is to low, exit the game and
    # output a suitable message
    play_again = "xxx"
    print("sorry, you have run out of money")
  else:
    play_again = input("Press Enter to play again "
                       "or 'xxx' to quit ")

print()
print("final balance", balance)
