# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:\Users\Abhilash\Documents\PROGRAMS_py\MIT 6.00.1x\ProblemSet3\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    for letter in secretWord:
        if letter not in lettersGuessed :
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    word=""
    for letter in secretWord:
        if letter not in lettersGuessed :
            word+="_ "
        else :
            word+=letter
    return word


def getAvailableLetters(lettersGuessed):
    from string import ascii_lowercase
    word=""
    for letter in ascii_lowercase :
        if letter not in lettersGuessed :
            word+=letter
    return word
    

def hangman(secretWord):
    lettersGuessed = []
    guess=8
    print ('Welcome to the game Hangman!\nI am thinking of a word that is '+str(len(secretWord))+' letters long.')
    print ('-------------')
    while guess > 0 :
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
        print ('You have '+str(guess)+' guesses left.\nAvailable letters: '+getAvailableLetters(lettersGuessed))
        letter = raw_input('Please guess a letter: ')
        letter = letter.lower()
        if letter not in getAvailableLetters(lettersGuessed) :
            print ("Oops! You've already guessed that letter: "),
        elif letter in secretWord :
            print ('Good guess: '),
            lettersGuessed+=letter
        else :
            print("Oops! That letter is not in my word: "),
            lettersGuessed+=letter
            guess-=1
        print getGuessedWord(secretWord, lettersGuessed)
        print ('-------------')
    if not isWordGuessed(secretWord, lettersGuessed) :
        print ("Sorry, you ran out of guesses. The word was "+secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = "else"
hangman(secretWord)
