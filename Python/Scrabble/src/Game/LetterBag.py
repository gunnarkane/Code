'''
Created on Mar 21, 2017

@author: gunnar
'''
from Game import Letter
import random

class letterBag:
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.letterSet = []
        self.createLetterSet()
    
    def createLetterSet(self):
        '''
        Creates a fresh dictionary with a full set of letters(key) and
        their corresponding points(values) for Scrabble
            
        E = ["E",1]
        A = ["A",1]
        I = ["I",1]
        O = ["O",1]
        N = ["N",1]
        R = ["R",1]
        T = ["T",1]
        L = ["L",1]
        S = ["S",1]
        U = ["U",1]
        D = ["D",4]
        G = ["G",2]
        B = ["B",3]
        C = ["C",3]
        M = ["M", 3]
        P = ["P",3]
        F = ["F",4]
        H = ["H",4]
        V = ["V",4]
        W = ["W",4]
        Y = ["Y",4]
        K = ["K",5]
        J = ["J",8]
        X = ["X",8]
        Q = ["Q",10]
        Z = ["Z",10]
        '''    
        
        for x in range(0,12):
            self.letterSet.append(Letter.letter("E", 1))
        for x in range(0,9):
            self.letterSet.append(Letter.letter("A", 1))
            self.letterSet.append(Letter.letter("I", 1))
        for x in range(0,8):
            self.letterSet.append(Letter.letter("O", 1))
        for x in range(0,6):
            self.letterSet.append(Letter.letter("N", 1))
            self.letterSet.append(Letter.letter("R", 1))
            self.letterSet.append(Letter.letter("T", 1))
        for x in range(0,4):
            self.letterSet.append(Letter.letter("L", 1))
            self.letterSet.append(Letter.letter("S", 1))
            self.letterSet.append(Letter.letter("U", 1))
            self.letterSet.append(Letter.letter("D", 4))
        for x in range(0,3):
            self.letterSet.append(Letter.letter("G", 2))
        for x in range(0,2):
            self.letterSet.append(Letter.letter("B", 3))
            self.letterSet.append(Letter.letter("C", 3))
            self.letterSet.append(Letter.letter("M", 3))
            self.letterSet.append(Letter.letter("P", 3))
            self.letterSet.append(Letter.letter("F", 4))
            self.letterSet.append(Letter.letter("H", 4))
            self.letterSet.append(Letter.letter("V", 4))
            self.letterSet.append(Letter.letter("W", 4))
            self.letterSet.append(Letter.letter("Y", 4))
     
        self.letterSet.append(Letter.letter("K", 5))  
        self.letterSet.append(Letter.letter("J", 8))
        self.letterSet.append(Letter.letter("X", 8))
        self.letterSet.append(Letter.letter("Q", 10))
        self.letterSet.append(Letter.letter("Z", 10))
     
    def lettersLeft(self):
        return len(self.letterSet)     
    
    def getLetters(self, number):
        lettersGiven = []
        for x in range(number):
            if len(self.letterSet) != 0:
                randomLetter = random.choice(self.letterSet)
                lettersGiven.append(randomLetter)
                self.letterSet.remove(randomLetter)
        return lettersGiven
    
    
