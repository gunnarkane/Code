'''
Created on Mar 30, 2017

@author: gunnar
'''
import math

def atheniumGrading(scores):
    '''
    Based on a list of scores these letter grades are assigned.
    * A score in the top 20% of all scores is an A.
    * A score in the next 20% of scores is a B. 
    * A score in the next 20% of scores is a C. 
    * A score in the next 20% of scores is a D. 
    * A score in the bottom 20% of scores is an F.
    @param: scores Original list of scores
    '''
    
    scoresWithGrades = []
    scoresLength = len(scores)
    sortedScores = sortScores(scores)
    interval = findInterval(scores)
    count = 0

    #while there are still letters that need letter grades assigned to them.
    while scoresLength > 0:
        #count dictates 20th, 40th, 60th, 80th, and 100th percentiles.
        if count == 0:
            for x in range(0,interval):
                finalGrade = ['A', sortedScores[x]]
                scoresWithGrades.append(finalGrade) 
                scoresLength -= 1
            count += 1 
        elif count == 1:
            for x in range(interval, interval*2):
                finalGrade = ['B', sortedScores[x]]
                scoresWithGrades.append(finalGrade)
                scoresLength -= 1
            count += 1
        elif count == 2:
            for x in range(interval*2, interval*3):
                finalGrade = ['C', sortedScores[x]]
                scoresWithGrades.append(finalGrade)
                scoresLength -= 1
            count += 1
        elif count == 3:
            for x in range(interval*3, interval*4):
                finalGrade = ['D', sortedScores[x]]
                scoresWithGrades.append(finalGrade)
                scoresLength -= 1
            count += 1
        elif count == 4:
            for x in range(interval*4, len(scores)):
                finalGrade = ['F', sortedScores[x]]
                scoresWithGrades.append(finalGrade)
                scoresLength -= 1
            count += 1
    
    sameScore(scoresWithGrades)
               
    return scoresWithGrades

def sortScores(unsortedScores):
    '''
    This method takes a list of whole numbers and sorts them in descending order 
    @param: unsortedScores A list of the orginial unsorted scores 
    '''
    sortedScores = sorted(unsortedScores, reverse=True)
    return sortedScores

def findInterval(scores):
    '''
    This method finds the 20% interval of a given list based on that lists length
    If the list is less than 5 items then the interval is automatically set to 1
    @param: scores A list of the scores unsorted or sorted. It does not matter
    '''
    interval = 0
    scoresLength = len(scores)
    
    interval = scoresLength * .2
    interval = math.floor(interval)# takes the floor of the interval because in a 2.2 interval, only the first two scores are considered in the top 20%. The 3rd score does not qualify.
    if interval == 0:
        interval = 1
    
    return interval 

def sameScore(scoresWithGrades):
    '''
    This method takes a list of scores that already have grades. If there are two
    identical scores with different letter grades, the lower letter grade is changed
    to the higher letter grade.
    @param: scoresWithGrades A list of lists containing a letter grade and score
    '''
    
    for x in range(len(scoresWithGrades) - 1):
        if scoresWithGrades[x][1] == scoresWithGrades[x+1][1]:
            scoresWithGrades[x+1][0] = scoresWithGrades[x][0]
    