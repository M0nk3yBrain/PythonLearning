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

#Write your code below this line 👇
import random

print("Welcome to rock paper sissors!")
userPlay = input("Rock = 0 Paper = 1 Scissors = 2. Ready? Set? Shoot! ")
userPlay = int(userPlay)
computerPlay = random.randint(0,2)
rps = [rock, paper, scissors]
player = rps[userPlay]
computer = rps[computerPlay]
print("You chose:\n",player)
print("Computer chose:\n",computer)
if userPlay == 0 and computerPlay == 2:
  print("You win!")
elif userPlay == 0 and computerPlay == 1:
  print("You lose!")
elif userPlay == 2 and computerPlay == 0:
  print("You lose!")
elif userPlay == 1 and computerPlay == 0:
  print("You win!")

elif userPlay == 2 and computerPlay == 1:
  print("You win!")
elif userPlay == 1 and computerPlay == 2:
  print("You lose!")
else:
  print("Tie!")
input("Press Enter to close")