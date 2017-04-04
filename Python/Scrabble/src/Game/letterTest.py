'''
Created on Mar 21, 2017

@author: gunnar
'''
import unittest
from Game import Letter

class letterTest(unittest.TestCase):


    def testLetterChar(self):
        e = Letter.letter("E", 1)
        self.assertTrue(e.getChar() == "E", "Constructor error: the letter is wrong")
        self.assertTrue(e.getValue() == 1, "Constructor error: the value is wrong")
        
    def testPringLetterList(self):
        letters = []
        letters.append(Letter.letter("J", 1))
        letters.append(Letter.letter("K", 2))
        
        #pring the list
        print(*letters)
        
        #print single item 
        print(str(letters[0]))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()