def Guesstries():
   for fn in range(1, 11):
      fg = int(input('Guess a number between 1 to 10: '))
      if fg == cg:
        print("Your Guess is Right, You Won!")
        break
      elif fg > cg:
        print("Your Guess is too high.")
      elif fg < cg:
        print("Your Guess is too Low.")


import random
ran = random.randint(1, 10)
cg: int = ran
# print(ran)
print("You will get only 10 chances to Guess the correct number! \n")
Guesstries()






