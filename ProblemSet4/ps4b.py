from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    max_score=0
    best_word=None
    for word in wordList:
        if isValidWord(word, hand, wordList):
            score=getWordScore(word, n)
            if score>max_score: 
                max_score=score
                best_word=word
    return best_word


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    score=0
    while calculateHandlen(hand) != 0:
        print ("Current Hand:"),
        displayHand(hand)
        word=compChooseWord(hand, wordList, n)
        if word is None: break
        score+=getWordScore(word, n)
        print ("\""+str(word)+"\" earned "+str(getWordScore(word, n))+" points. Total: "+str(score)+" points\n")
        hand=updateHand(hand, word)
    print ("Total score: "+str(score)+" points.")
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    hand={}
    choice='a'
    while choice is not 'e':
        choice=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if choice is 'n':
            hand=dealHand(HAND_SIZE)
            player='a'
            while player is not 'u' and player is not 'c':
                player=raw_input("Enter u to have yourself play, c to have the computer play: ")
                if player is 'u':
                    playHand(hand, wordList, HAND_SIZE)
                elif player is 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print "Invalid command."
        elif choice is 'r':
            if hand == {}:
                print "You have not played a hand yet. Please play a new hand first!"
            else:
                player='a'
                while player is not 'u' and player is not 'c':
                    player=raw_input("Enter u to have yourself play, c to have the computer play: ")
                    if player is 'u':
                        playHand(hand, wordList, HAND_SIZE)
                    elif player is 'c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                    else:
                        print "Invalid command."
        elif choice is not 'e':
            print "Invalid command."
        print "\n"

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


