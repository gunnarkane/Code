'''
Created on Mar 5, 2017

@author: gunnar
'''

class board:
    '''
    Creates a fresh scrabble Board
    '''
    
    def __init__(self):
        '''
        Constructor: Creates a 15 x 15 board with a star in the middle to designate the starting square
        '''
        self.board = [[0for x in range(15)] for y in range(15)]
        for x in range(15):
            for y in range(15):
                self.board[x][y] = "-"
                
        self.board[7][7] = "*" 
        
    def printBoard(self):
        '''
        This method prints the board. The extra spacing to help number rows and columns 
        '''
        print("     ", end = "")
        for x in range(9):
            print(x + 1, end = "    ")
        for x in range(6):
            print(x + 10, end = "   ")
        print("\n", end = "")  
        #format
        for x in range(9):
            print(x + 1,"", self.board[x])
        for x in range(6):
            print(x + 10, self.board[x + 9]) 
        print("\n")
          
    
    def addLetters(self, newLetters, locationX, locationY, direction):
        '''
        This method adds the letters to the board in three different directions
        @param: newLetters are the letters to be added to the board
        @param: locationX is row 
        @param: locationY is the column 
        @param: direction is the directions the word is inserted
        '''
        locationX -= 1
        locationY -= 1
        if direction == 'right' and (locationX + len(newLetters) <= 15):      
            for x in range(len(newLetters)):
                self.board[locationX][locationY + x] = newLetters[x].getChar()
        elif direction == 'up' and (locationY - len(newLetters) >= 0):
            for x in range(len(newLetters)):
                self.board[locationX - x][locationY] = newLetters[x].getChar()
        elif direction == 'down' and (locationY + len(newLetters) <= 15):
            for x in range(len(newLetters)):
                self.board[locationX + x][locationY] = newLetters[x].getChar()
        else:
            print("You cannot play that word")
            
            
            
            
