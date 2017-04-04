'''
Created on Mar 12, 2017

@author: gunnar
'''
import unittest
from Game import Player, Letter



class playerTest(unittest.TestCase):

    def testPlayerConstructor(self):
        joe = Player.player("Joe")
        self.assertTrue((joe.getName() == "Joe"), "constructor failed: name")
        self.assertTrue((joe.getScore() == 0), "constructor failed: score")
        self.assertTrue((joe.letterCount() == 0), "constructor failed: list of letters")
    
    def testSetScore(self):
        joe = Player.player("Joe")
        joe.setScore(250)
        self.assertTrue(joe.getScore() == 250, "set Score fail")

    def testAddLetter(self):
        joe = Player.player("Joe")
        list = []
        e = Letter.letter('E', 1)
        d = Letter.letter('D', 2)
        
        for x in range(4):
            list.append(e)
        for x in range(3):    
            list.append(d)
            
        joe.addLetters(list)
        
        self.assertTrue(joe.getLetters()[0] == e, "set letter fail")
        self.assertTrue(joe.getLetters()[4] == d, "set letter fail")
        
    def testGetLetters(self):
        joe = Player.player("Joe")
        list = []
        e = Letter.letter('E', 1)
        d = Letter.letter('D', 2)
        
        for x in range(4):
            list.append(e)
        for x in range(3):    
            list.append(d)
            
        joe.addLetters(list)
        
        self.assertTrue(joe.getLetters() == [e,e,e,e,d,d,d], "getLetters does not work")

    def testletterCount(self):
        joe = Player.player("Joe")
        list = []
        e = Letter.letter('E', 1)
        d = Letter.letter('D', 2)
        
        for x in range(4):
            list.append(e)
        for x in range(3):    
            list.append(d)
            
        joe.addLetters(list)
        
        self.assertTrue(joe.letterCount() == 7, "letterCount does not work")
        
    def testPrintLetters(self):
        joe = Player.player("Joe")
        list = []
        e = Letter.letter('E', 1)
        d = Letter.letter('D', 2)
        
        for x in range(4):
            list.append(e)
        for x in range(3):    
            list.append(d)
            
        joe.addLetters(list)
        
        joe.printLetters()
    
    def testgetWord(self):
        joe = Player.player("Joe")
        list = []
        e = Letter.letter('E', 1)
        d = Letter.letter('D', 2)
        
        for x in range(4):
            list.append(e)
        for x in range(3):    
            list.append(d)
            
        joe.addLetters(list)
        print("\n")
        word = joe.getWord('DEED')
        
        self.assertTrue(joe.letterCount() == 3, "letterCount did not work")
        self.assertTrue(len(word) == 4, "getWord is wrong")
        self.assertTrue(word[0].getChar() == 'D', "getWord doesnt work")
        self.assertTrue(word[0].getValue() == 2, "getWord doesnt work")
        self.assertTrue(word[1].getChar() == 'E', "getWord doesnt work")
        self.assertTrue(word[1].getValue() == 1, "getWord doesnt work")
        self.assertTrue(word[2].getChar() == 'E', "getWord doesnt work")
        self.assertTrue(word[2].getValue() == 1, "getWord doesnt work")
        self.assertTrue(word[3].getChar() == 'D', "getWord doesnt work")
        self.assertTrue(word[3].getValue() == 2, "getWord doesnt work")
        for letter in word:
            print(letter.getChar())
        print("\n")
        joe.printLetters()
        
    '''
    def testAddScore(self):
        joe = Player.player("Joe")
        list = []
        e = Letter.letter('E', 1)
        d = Letter.letter('D', 2)
        
        for x in range(4):
            list.append(e)
        for x in range(3):    
            list.append(d)
            
        joe.addLetters(list)
        joe.useLetters(list)
        joe.addScore(list)
        joe.printScore()
    '''   
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()