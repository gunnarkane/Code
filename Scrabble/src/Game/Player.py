'''
Created on Mar 1, 2017

@author: gunnar
'''
from Game import Letter
class player:
    '''
    defines a player class who has a set of letters, score, and a name. 
    '''
        
    def __init__(self, name):
        '''
        define the set of letters which are taken from the pile of letters.
        define the score of 0.
        define the name which is given.
        '''
        self.name = name 
        self.score = 0
        self.letters = []
        
    def getName(self):
        '''
        Returns the name of the Player
        '''
        return self.name
    
    def setScore(self, score):
        '''
        Sets the score of the Player
        @param: score is the player's new score
        '''
        self.score = score
    
    def getScore(self):
        '''
        Returns the score of the Player
        '''
        return self.score
    
    def getLetters(self):
        '''
        Returns the letters the Player currently has to use
        '''
        return self.letters
    
    def addLetters(self, newLetters):
        '''
        Adds new letters to the players current letters he can use to play
        @param: newLetters is a list of the new letters given to the player
        '''
        if len(newLetters) == 7 - self.letterCount():
            self.letters = self.letters + newLetters

    def getWord(self, givenLetters):
        '''
        This method validates, and removes the letters needed to make the
        word that the player wants to play
        @param: givenLetters is a list of letters that make up the specific word
        '''
        listString = list(givenLetters)
        listLetter = []
        for x in listString:
            found = False
            for letter in self.letters:
                if (x == letter.getChar()):
                    found = True
                    newLetter = Letter.letter(letter.getChar(), letter.getValue())
                    listLetter.append(newLetter)
                    break
            if not found:
                listLetter = []
                return listLetter
            
        for letterX in listLetter:
            for letterY in self.letters:
                if letterX.getChar() == letterY.getChar():
                    self.letters.remove(letterY)
                    break
                
        return listLetter
                
    def letterCount(self):
        '''
        Returns the length of the Players letters
        '''
        return len(self.letters)
    
    def addScore(self, usedLetters):
        '''
        This method adds a score based on a played word to a player
        @param: usedLetters is the word that was successfully played
        '''
        for letter in usedLetters:
            self.score += letter.value

    def printLetters(self):
        '''
        Prints the players list of playable letters showing the score and char 
        '''
        for letter in self.letters:
            print(letter.getChar(), letter.getValue())
    
    def printScore(self):
        '''
        Prints the players current score
        '''
        score = str(self.score)
        print(self.getName() + " your score is: " + score)


    