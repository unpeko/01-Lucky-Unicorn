import random

# main routine goes here
tokens = ["unicorn", "horse", "zebra", "donkey"]
starting_balance = 100

balance = starting_balance
# Testing loop to generate 20 tokens
for item in range(0,100):
  chosen_num = random.randint(1, 100)

  # adjust balance 
  if 1 <= chosen_num <= 5:
    chosen = "unicorn"
    balance += 4
  elif 6 <= chosen_num <= 36:
    chosen = "donkey"
    balance -= 1
  else:
    if chosen_num % 2 == 0:
      chosen = "horse"
    else: 
      chosen = "zebra"
    balance -= 0.5

  # output
  print("You got a {}.  Your balance is " 
       "${:.2f}".format(chosen, balance))
print()