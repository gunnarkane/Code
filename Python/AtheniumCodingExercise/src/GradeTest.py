'''
Created on Mar 30, 2017

@author: gunnar
'''
import unittest
from Grade import atheniumGrading, findInterval, sameScore, sortScores

class Test(unittest.TestCase):

    def testAtheniumGrading(self):
        scores1 = [99, 92, 91, 91, 89, 85, 83, 82, 80, 79, 78, 78, 77, 76, 75, 74, 62, 55, 43, 20]
        grades1 = atheniumGrading(scores1)
        print(grades1)
        scores2 = [99,99,99,99,99,99,99,99,99,99,99,99,98] 
        grades2 = atheniumGrading(scores2)
        print(grades2)
        scores3 = [3,2,1]
        grades3 = atheniumGrading(scores3)
        print(grades3)
        scores4 = [1,2,3,7,88,99,4,9,100,4,12]
        grades4 = atheniumGrading(scores4)
        print(grades4)
        
        self.assertTrue(grades1[0][0] == 'A' and grades1[4][0] == 'B'and grades1[8][0] == 'C' and grades1[12][0] == 'D' and grades1[16][0] == 'F', 'Your findInterval function is broken' )
        self.assertTrue(grades2[0][0] == 'A' and grades2[9][0] == 'A' and grades2[12][0] == 'F' , 'the sameScore function is broken')
        self.assertTrue(grades3[0][0] == 'A' and grades3[1][0] == 'B' and grades3[2][0] == 'C', 'lists less than 5 cannot be handled')
        self.assertTrue(grades4[0][0] == 'A', 'the sortScores function is broken')
    
    def testFindInterval(self):
        scores1 = [99, 92, 91, 91, 89, 85, 83, 82, 80, 79, 78, 78, 77, 76, 75, 74, 62, 55, 43, 20]
        scores2 = [3,2,1]
        scores3 = [1,2,3,7,88,99,4,9,100,4,12]
        
        self.assertTrue(findInterval(scores1) == 4, 'The interval is wrong')
        self.assertTrue(findInterval(scores2) == 1, 'The interval is wrong')
        self.assertTrue(findInterval(scores3) == 2, 'The interval is wrong')
        
    def testSortScores(self):
        scores = [1,4,9,22,10009,8,77,99,99,99,88,22,11,33,54326]
        sortedScores = sortScores(scores)
        print(sortedScores)
        
        self.assertTrue(sortedScores[0] == 54326 and sortedScores[14] == 1, 'sortScores is broken')
        
    def testSameScore(self):
        grades = [['A',99],['B',99],['C',99],['D',99],['F',99],['F',99],['F',98]]
        sameScore(grades)
        
        self.assertTrue(grades[0][0] == 'A' and grades[5][0] == 'A' and grades[6][0] == 'F' , 'the sameScore function is broken')
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAtheniumGrading']
    unittest.main()