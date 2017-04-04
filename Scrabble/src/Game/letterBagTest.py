'''
Created on Mar 21, 2017

@author: gunnar
'''
import unittest
from Game import LetterBag

class letterBagTest(unittest.TestCase):

    def testCreateLetterSet(self):
        letterBag = LetterBag.letterBag()
        self.assertTrue((letterBag.lettersLeft() == 98), "constructor failed: number of letters wrong")
    
    def testLettersLeft(self):
        letterBag = LetterBag.letterBag()
        print(letterBag.lettersLeft())  
        
    def testGetLetters(self):
        letterBag = LetterBag.letterBag()
        ranLetters = letterBag.getLetters(5)
        moreRanLetters = letterBag.getLetters(5)
        self.assertTrue(letterBag.lettersLeft() == 88, "getLetters is not subtracting letters ")
        self.assertTrue(ranLetters != moreRanLetters, "the letters are not random")  
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    