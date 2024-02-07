from random import randint
from art import logo

EASY_LIVES_COUNT = 10
HARD_LIVES_COUNT = 5


def difficultySelector():
    difficultyText = input("Pick a difficulty 'Easy' or 'Hard': ")
    difficulty = difficultyText.lower()
    if difficulty == "easy":
        return EASY_LIVES_COUNT
    if difficulty == "hard":
        return HARD_LIVES_COUNT


def guessChecker(lives, answer):
    loop = True
    while lives != 0 and loop is True:
        guess = int(input("Now pick a number from 1 - 100: "))
        if guess > answer:
            print("Lower")
            lives -= 1
            print(f"Lives remaining: {lives}")
        elif guess < answer:
            print("Higher")
            lives -= 1
            print(f"Lives remaining: {lives}")
        else:
            print(f"Your guess is correct! The number was {answer}")
            loop = False
    if lives is 0:
        print(f"You lose. The number was {answer}")


def gameLoop():
    print(logo)
    print("Welcome to High or Low")
    answer = randint(1, 100)
    print("You will be picking a number from 1-100")
    lives = difficultySelector()
    print(f"You will have '{lives}' chances to guess the number.")
    guessChecker(lives, answer)
    playAgain()


def playAgain():
    replay = input(f"Would you like to play again? Yes or No? ")
    replaylower = replay.lower()
    if replay == "yes":
        gameLoop()


gameLoop()
