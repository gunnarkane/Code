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
        return self.name
    
    def setScore(self, score):
        self.score = score
    
    def getScore(self):
        return self.score
    
    def getLetters(self):
        return self.letters
    
    def addLetters(self, newLetters):
        if len(newLetters) == 7 - self.letterCount():
            self.letters = self.letters + newLetters

    def getWord(self, givenLetters):
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
        return len(self.letters)
    
    def addScore(self, usedLetters):
        for letter in usedLetters:
            self.score += letter.value

    def printLetters(self):
        for letter in self.letters:
            print(letter.getChar(), letter.getValue())
    
    def printScore(self):
        score = str(self.score)
        print(self.getName() + " your score is: " + score)


    