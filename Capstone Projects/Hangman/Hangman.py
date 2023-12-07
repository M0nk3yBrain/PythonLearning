import random
import hangmanArt
import hangmanWords

# Number of lives and will tie back into the ASCII art variable stages[]
lives = 6

# Display will show the current amount of blank spaces and update as player guesses their letters
display = []

# Chooses random word from wordbank under the variable wordList
chosenWord = random.choice(hangmanWords.wordList)

# Tracks end of game state
endOfGame = False

# Grabs the word length number to help optomize code.
wordLength = len(chosenWord)
for _ in range(wordLength):
  display += "_"

#print(f'The chosen word is: {chosenWord}')
print(hangmanArt.logo)
replay = True
previousGuess = [""]

while not endOfGame:
    print("Previously Guessed Letters:")
    print(f"{' '.join(previousGuess)}")
    guess = input("Guess a letter:\n").lower()
    if guess not in previousGuess:
        previousGuess.append(guess)
  # Checks the word to see if the letter is in the chosenWord variable.
        for position in range(wordLength):
            letter = chosenWord[position]
            if letter == guess:
                display[position] = letter
        if guess not in display:
            lives -= 1
            print(f"{guess}: is not in the word.")
            if lives == 0:
                endOfGame = True
        if '_' not in display:
            endOfGame = True
        print(f"{' '.join(display)}")
        print(f"{hangmanArt.stages[lives]}")
    else:
        print(f"{hangmanArt.stages[lives]}")
        print(f"You have already guessed the letter: {guess}. Please make another guess")

if lives != 0:
  print("Congratulations! You win!")
else:
  print(f"You lose. The word was: {chosenWord}")
press = input("Press Enter to close")