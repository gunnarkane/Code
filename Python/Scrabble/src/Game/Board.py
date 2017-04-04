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
        #starting at 10 there is anextra space that needed formatting
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
          
    # must add condition for is using letters already on the board  
    # also add condition for letters to left. must reverse order of letters so word reads left to right      
    def addLetters(self, newLetters, locationX, locationY, direction):
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
            
            
            
            
