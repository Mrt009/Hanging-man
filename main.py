# This is Hangman game. Computer randomly picks a word, and player needs to
# guess what is the word. The player also has to guess the word before
# hangman is completely drawn.
# Check also flowchart.pdf for more info.

from random import randint
from hangs import HANGMAN_PICS # Imports list of Hangman drawings

def main():
    gameEnd = False

    while gameEnd == False:
        playGame()

        # Ask if user would like to play again
        while True:
            decision = input('Would you like to play again? (yes or no): ').lower()
            if decision == 'yes':
                break
            if decision == 'no':
                gameEnd = True
                break

def playGame():
    ''' Plays one Hangman game '''
    # Initial values
    secretWord = pick_word()
    guessedLetters = ['_'] * len(secretWord)
    wrongLetters = ''

    print('\n' * 2 + 'H A N G M A N')

    while True:
        print('\n' + 'Secret word: ' + ' '.join(guessedLetters).capitalize())
        print('Wrong letters: ' + ' '.join(wrongLetters))
        print(HANGMAN_PICS[len(wrongLetters)])

        # Check winning or losing status
        if ''.join(guessedLetters).isalpha():
            print('You won! :)')
            break
        if len(wrongLetters) >= len(HANGMAN_PICS) - 1:
            print('You lost! :(. It was {}'.format(secretWord.title()))
            break

        inputLetter = getLetter()

        # Check if user guessed the letter
        if inputLetter in secretWord:
            for charNum in range(len(secretWord)):
                if inputLetter == secretWord[charNum]:
                    # Add letter to guessed letters
                    guessedLetters[charNum] = inputLetter
        # Check if user already typed this letter
        elif inputLetter in wrongLetters:
            print('You have already typed this letter!')
        # Else add to wrong letters
        else:
            wrongLetters = wrongLetters + inputLetter

def getLetter():
    '''
    Gets letter from user as input and validates if the input
    is actually a letter.
    '''

    while True:
        letter = input('Guess a letter: ')
        if len(letter) == 1 and letter.isalpha() == True:
            return letter.lower()


def pick_word():
    '''
    Creates a list of words with minimum three letters from file.
    Picks and returns random word from the list.
    '''

    filePath = 'words.txt'
    file = open(filePath, 'r')
    words = []

    # Add words with min three characters
    for line in file:
        line = line.rstrip('\n')
        if len(line) >= 3:
            words.append(line.lower())

    file.close()

    # Draw random word from the list
    word = words[randint(0, len(words))]
    return word

if __name__ == '__main__':
    main()

