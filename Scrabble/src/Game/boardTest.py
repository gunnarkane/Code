'''
Created on Mar 12, 2017

@author: gunnar
'''
import unittest
from Game import Board
from Game import Letter

class boardTest(unittest.TestCase):

    def testPrintBoard(self):
        scrabbleBoard = Board.board()
        scrabbleBoard.printBoard()

    def testaddLetters(self):
        scrabbleBoard = Board.board()
        letterList = []
        
        g = Letter.letter('G', 2)
        letterList.append(g)
        u = Letter.letter('U', 1)
        letterList.append(u)
        n = Letter.letter('N', 1)
        letterList.append(n)
        letterList.append(n)
        a = Letter.letter('A', 1)
        letterList.append(a)
        r = Letter.letter('R', 1)
        letterList.append(r)
        
        scrabbleBoard.addLetters(letterList, 8, 8, 'right')
        scrabbleBoard.addLetters(letterList, 8, 8, 'up')
        scrabbleBoard.addLetters(letterList, 8, 8, 'down')
        scrabbleBoard.printBoard()
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    