'''
Created on Mar 1, 2017

@author: Gunnar Kane
'''
from Game import Board, LetterBag, Player
from _dummy_thread import exit
import copy 

def main():
    '''
    Starts the Scrabble game
    '''
    answer = input('Would you like to play Scrabble? Please type Yes/yes or No/no. Then press enter.\n')
    while answer !='yes' and answer !='Yes' and answer !='No' and answer != 'no':
        answer = input('Please answer Yes/yes or No/no and then press enter. Would you like to play Scrabble?\n')
    
    if(answer == 'yes' or answer == 'Yes'):
        startGame()   
    else:
        print('Thats okay, have a nice day.\nBye!')
        exit

def startGame():
    '''
    This function handles the game flow from start to finish.
    '''
    scrabbleBoard = Board.board()
    letterBag = LetterBag.letterBag()
    
    playerList = makePlayers()   
    for player in playerList: 
        startLetters = letterBag.getLetters(7) 
        player.addLetters(startLetters)
        print('\nHi', player.name, 'here are your seven letters to start with.')
        player.printLetters()
        print("\n")
    
    originPlayers = copy.copy(playerList)# made deep copy of players for setting and printing players scores at the end of the game
    
    playerNum = 0
    while len(playerList) > 1:
        wordLetter = nextTurn(playerList[playerNum], scrabbleBoard)
        if not wordLetter:
            playerList.remove(playerList[playerNum])
        else:
            print("\n")
            answer = input("Please give the row, column, and direction you would like to play the word and then press enter."
            + " The parameters are separated by spaces Ex: 7 8 up")
            splitAnswer = answer.split(" ")
            locationX = int(splitAnswer[0])
            locationY = int(splitAnswer[1])
            direction = splitAnswer[2]
            scrabbleBoard.addLetters(wordLetter, locationX, locationY, direction)
            newLetters = letterBag.getLetters(len(wordLetter))
            playerList[playerNum].addLetters(newLetters)
            playerList[playerNum].addScore(wordLetter)
            playerList[playerNum].printScore()
            playerNum += 1
            
        if playerNum == len(playerList):
            playerNum = 0
            
    print("The game has ended due to the fact that there are not at least 2 players still playing.\n")
    
    for player in originPlayers:
        print(player.getName(), "had a score of ", player.getScore())
                 
def nextTurn(player, scrabbleBoard):
    '''
    This method controls a single player's turn
    @param: player is the current player
    @param: is the current Scrabble Board
    '''
    scrabbleBoard.printBoard()
    print(player.getName(), "It's your turn. Using your letters, enter the word you want to play in all CAPS."
          + " Type the word quit and press enter to stop playing.")
    player.printLetters()
    word = input()
    wordString = list(word)
    wordLetter = []
    if word == "quit":
        print(player.getName() + ": You are done playing Scrabble")
    else:
        wordLetter = player.getWord(wordString)# need to pass in list of letters based on user input not list of characters, use index as input
    return wordLetter

def makePlayers():
    playerList = []
    numPlayers = int(input("The game of Scrabble has started, how many players are their?**2-4**. Type 2, 3, or 4, then press enter.\n"))
    while numPlayers < 2 or numPlayers > 4:
        numPlayers = int(input("Please enter a valid number between 2 and 4, how many players are their?\n"))
    for x in range(numPlayers):
        print('What is your name player', x + 1, '?')
        name = input()
        playerList.append(Player.player(name))
    return playerList          

if __name__ == "__main__":
    main()
    
    
    
    
    