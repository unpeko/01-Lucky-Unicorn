import random

# main routine goes here
tokens = ["unicorn", "horse", "horse", "horse", 
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey"]
starting_balance = 100

balance = starting_balance
# Testing loop to generate 20 tokens
for item in range(0,500):
  chosen = random.choice(tokens)

  # adjust balance 
  if chosen == "unicorn":
    balance += 4
  elif chosen == "donkey":
    balance -= 1
  else:
    balance -= 0.5

  # output
  print("You got a {}.  Your balance is " 
       "${:.2f}".format(chosen, balance))
print()