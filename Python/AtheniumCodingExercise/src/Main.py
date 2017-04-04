'''
Created on Mar 30, 2017

@author: gunnar
'''
from Grade import atheniumGrading

def main():

    scores1 = [99, 92, 91, 91, 89, 85, 83, 82, 80, 79, 78, 78, 77, 76, 75, 74, 62, 55, 43, 20]
    grades1 = atheniumGrading(scores1)
    print(grades1)
    print('\n')
    
    scores2 = [99,99,99,99,99,99,99,99,99,99,99,99,98] 
    grades2 = atheniumGrading(scores2)
    print(grades2)
    print('\n')
    
    scores3 = [3,2,1]
    grades3 = atheniumGrading(scores3)
    print(grades3)
    print('\n')
    
    scores4 = [1,4,4,7,88,99,4,9,100,4,12]
    grades4 = atheniumGrading(scores4)
    print(grades4)
    print('\n')
   
if __name__ == '__main__':
    main()