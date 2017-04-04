'''
Created on Mar 1, 2017

@author: gunnar
'''

class letter:
    '''
    This class will hold the character and value of a letter in scrabble
    '''

    def __init__(self, char, value):
        '''
        When a letter is created, then a character and value will be set
        '''
        self.char = char
        self.value = value
        
    def getChar(self):
        '''
        Returns the char value of the Letter Object
        '''
        return self.char
    
    def getValue(self):
        '''
        Returns the point value of the Letter Object
        '''
        return self.value
    
    def __str__(self):
        '''
        equivalent to toString() in java
        '''
        return '[' + self.char + ',' + str(self.value) + ']'