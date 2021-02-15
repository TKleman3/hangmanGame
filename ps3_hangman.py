# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return set(secretWord).issubset(lettersGuessed) 



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    revealed = []
    for l in secretWord:
          if l in lettersGuessed:
              revealed.append(l)
          else:
              revealed.append('_ ')
    return ''.join(revealed)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    letters = [l for l in string.ascii_lowercase if l not in lettersGuessed]
    return ''.join(letters)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    import string

    playing = True
    mistakesMade = 8
    lettersGuessed = []
    print('Welcome to the game, Hangman!')
    print('The secret word has ' + str(len(secretWord)) + ' letters.') 
    print('------------------')
    while playing:
    # Shows how many guesses left and takes user input per round. Turns guess into a lower case letter
      print("You have " + str(mistakesMade) + " guesses left.")
      print('Available letters: ' + getAvailableLetters(lettersGuessed))
      guess = input(str('Please guess a letter: ')).lower()
    #Checks to make sure only one letter was entered
      while len(guess) != 1 or guess not in string.ascii_lowercase: 
        print('Please enter only one letter, and only letters!')
        guess = input(str('Please guess a letter: ')).lower()
    #Checks to see if guess is in secret word or not, prints out current letters in secret word
      if guess in lettersGuessed:
        print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord,lettersGuessed))
        print('------------------')
      elif guess in secretWord:
        lettersGuessed += [guess]
        print("Good guess: " + getGuessedWord(secretWord,lettersGuessed))
        print('------------------')
      else:
        lettersGuessed += [guess]
        print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
        mistakesMade -= 1
        print('------------------')
    #Check win and lose condition
    #win condition
      if isWordGuessed(secretWord,lettersGuessed):
        print('Congratulations, you won!')
        playing = False
    #lose condition
      if mistakesMade == 0:
        print("Sorry, you ran out of guesses. The word was " + secretWord + '.')
        playing = False

 
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
