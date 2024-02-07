import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

playerHand = []
dealerHand = []
handTotal = 0
playerBust = False
dealerBust = False


# Draw card for both Player and dealer
def drawCard():
    cardIndex = random.randrange(0, 13)
    return cards[cardIndex]


def addPlayer():
    playerHand.append(drawCard())


def addDealer():
    dealerHand.append(drawCard())


# Draw initial hands for Player and Dealer Then displayes them
def getHands():
    for _ in range(2):
        addPlayer()
        addDealer()
    print(f"Your hand is: {playerHand[0]} {playerHand[1]}")
    print(f"Dealer hand is: {dealerHand[0]}")


# Count the total in Player hand
def playerTotal(playerHand):
    total = sum(playerHand)
    return total


def dealerTotal(dealerHand):
    total = sum(dealerHand)
    return total


# Main game loop
def gameloop():
    playerBust = False
    dealerBust = False
    continueDraw = True
    dealer = dealerTotal(dealerHand)
    while not playerBust and continueDraw:
        player = playerTotal(playerHand)
        print(f"Your current total is: {player}")
        if player > 21:
            if 11 in playerHand:
                print("Player would bust but has an 'Ace'. Dropping to 1.")
                playerHand.remove(11)
                playerHand.append(1)
            else:
                playerBust = True
                print("Player Bust. You Lose.")
        else:
            draw = input(
                "Do you want to draw another card? Type 'hit' to draw 'pass' to stop: "
            )
            if draw == "hit":
                addPlayer()
            elif draw == "pass":
                continueDraw = False
            else:
                print("Please type either 'hit' or 'pass': ")
    if playerBust is not True:
        print(f"Dealer total is {dealer}")
        player = playerTotal(playerHand)
        while not dealerBust and player > dealer:
            print("Dealer draws a card.")
            addDealer()
            dealer = dealerTotal(dealerHand)
            print(f"Dealer total is {dealer}")
            if dealer > 21:
                if 11 in dealerHand:
                    print("Dealer would bust but has an 'Ace'. Dropping to 1.")
                    dealerHand.remove(11)
                    dealerHand.append(1)
                    dealer = dealerTotal(dealerHand)
                else:
                    dealerBust = True
                    print("Dealer Bust. You Win.")


def results():
    player = playerTotal(playerHand)
    dealer = dealerTotal(dealerHand)
    if player < 22 and player > dealer:
        print(f"You Win!\nPlayer: {player}\nDealer: {dealer}")
    elif dealer < 22 and dealer > player:
        print(f"You Lose.\nDealer: {dealer}\nPlayer: {dealer}")
    else:
        print("On Ties Dealer Wins")
        print(f"Dealer: {dealer}\nPlayer: {player}")


# Start of Program
getHands()
gameloop()
results()

# https://www.gdquest.com/tutorial/godot/learning-paths/beginner/
# https://www.gdquest.com/tutorial/getting-started/learn-to/choosing-a-game-engine/
# https://docs.python-guide.org/intro/learning/
# https://gdquest.github.io/learn-gdscript/#course/lesson-2-your-first-error/lesson.tres
