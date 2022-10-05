
class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numberical Tic Tac Toe board.
        Inputs: none
        Returns: None
        ''' 
        self.board = [] # create a list
        self.size = 3   # 3*3 row and column
        self.type = "number"
       
        
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(float('inf'))
            self.board.append(row)
        
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''

        print('%3s %3s %3s \t'%("0","1","2")) #print the first row for number
        for row in range(3):
            if row > 0 :
                print('-----------')
            print(row, end=" ")
            for col in range(3) :
                if col > 0 :
                    print('|', end='')
                print(' ', end='')
                if self.board[row][col] == float('inf'):#use space padding the board,aviod the occurrence of def isWinner include "0"
                    print(' ', end='')
                else :
                    print(self.board[row][col], end='')
                print('', end='')
            print()



    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        # TO DO: delete pass and complete method
        if self.board[row][col] != float('inf'):
            return False
        else:
            return True



    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
            row (int) - row index of square to update
            col (int) - column index of square to update
            num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        # TO DO: delete pass and complete method
        if self.squareIsEmpty(row, col):
            self.board[row][col] = num#return to local board
            return True
        else:
            return False
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        # TO DO: delete pass and complete method
        Full = False
        for row in range(3):
            for col in range(3):
                if self.squareIsEmpty(row,col):#if the board has empty, the board is not full.
                    return False
        return True
        
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # TO DO: delete pass and complete method
        for row in range(3):
            if float(self.board[row][0]) + float(self.board[row][1]) + float(self.board[row][2]) == 15:#determine the row
                return True
        for col in range(3):
            if float(self.board[0][col]) + float(self.board[1][col]) + float(self.board[2][col]) == 15:#determine the column
                return True
        if float(self.board[0][0]) + float(self.board[1][1]) + float(self.board[2][2]) == 15: #determine the right slash
            return True
        elif float(self.board[2][0]) + float(self.board[1][1]) + float(self.board[0][2]) == 15:#determine the left slash
            return True
        else:
            return False

       
    
    def isNum(self):
        '''
        Checks whether this is a Numberical Tic Tac Toe board or not
        Inputs: none
        Returns: True
        '''
        # TO DO: delete pass (and this comment) and complete method
            
        return self.type == "number" #the localboard is numerical board
        for row in range(3):
            for col in range(3):
                if type(self.board[row][col]) == self.type:
                    return True  
    
class ClassicTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Classic Tic Tac Toe board.
        Inputs: none
        Returns: None
        ''' 
        # TO DO: delete pass (and this comment) and complete method
        self.board = [] # create a list
        self.size = 3   # 3*3 row and column
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(float('inf'))
            self.board.append(row)
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''

        print('%3s %3s %3s \t'%("0","1","2"))
        for row in range(3):
            if row > 0 :
                print('-----------')
            print(row, end=" ")
            for col in range(3) :
                if col > 0 :
                    print('|', end='')
                print(' ', end='')
                if self.board[row][col] == float('inf'):#use space padding the board
                    print(' ', end='')
                else :
                    print(self.board[row][col], end='')
                print('', end='')
            print()


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is "empty", or if it already contains an X or O.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        if self.board[row][col] != float('inf'):
            return False
        else:
            return True
    
    
    def update(self, row, col, mark):
        '''
        Assigns the string, mark, to the board at the provided row and column, 
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
         # TO DO: delete pass (and this comment) and complete method
        if self.squareIsEmpty(row, col):
            self.board[row][col] = mark #return to local board
            return True
        else:return False
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        Full = False
        for row in range(3):
            for col in range(3):
                if self.squareIsEmpty(row,col):#if the board has empty, the board is not full.
                    return False
        return True
                # else:
                #   return True

           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) with 
        matching marks (i.e. 3 Xs  or 3 Os). That line can be horizontal, vertical,
        or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        ''' 
        for row in range(3):
            
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == "X" or self.board[row][0] == self.board[row][1] == self.board[row][2] == "O":#determine the row
                return True

            
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == "X" or self.board[0][col] == self.board[1][col] == self.board[2][col] == "O":#determine the column
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == "X" or self.board[0][0] == self.board[1][1] == self.board[2][2] == "O":#determine the right slash
            return True
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] == "X" or self.board[2][0] == self.board[1][1] == self.board[0][2] == "O":#determine the left slash
            return True
        else:
            return False


    def isNum(self):
        '''
        Checks whether this is a Numberical Tic Tac Toe board or not
        Inputs: none
        Returns: False
        '''
        # TO DO: delete pass (and this comment) and complete method
        
        return False #the board not numerical board, return False


class MetaTicTacToe:
    def __init__(self,configFile):
        '''
        Initializes an empty Meta Tic Tac Toe board, based on the contents of a 
        configuration file.
        Inputs: 
           configFile (str) - name of a text file containing configuration information
        Returns: None
        ''' 
        # TO DO: delete pass (and this comment) and complete method
        
        configFile = ['c', 'c', 'n'],['c', 'n', 'c'],['n', 'c', 'n']
        self.board = configFile
        self.current_player = 1
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        # TO DO: delete pass (and this comment) and complete method

        print('%3s %3s %3s \t'%("0","1","2"))
        for i in range(3) :
            if i > 0 :
                print('  -----------')
            print(i, end=" ")
            for j in range(3) :
                if j > 0 :
                    print('|', end='')
                print(' ', end='')
                if self.board[i][j] == float('inf'): #use the space padding the board
                    print(' ', end='')
                else :
                    print(self.board[i][j], end='')
                print(' ', end='')
            print()


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square contains a non-played local game board ("empty"),
        or the result of a played local game board (not "empty").
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        if self.board[row][col] == 'c':
            return True
        if self.board[row][col] == 'n':
            return True


    
    
    def update(self, row, col, result):
        '''
        Assigns the string, result, to the board at the provided row and column, 
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           result (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
         # TO DO: delete pass (and this comment) and complete method
        if self.squareIsEmpty(row,col): 
            self.board[row][col] = result#return to globle board
            return True
        else:
            return False

    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares (i.e. any un-played
        local boards).
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        
        Full = False
        for row in range(3):
            for col in range(3):
                if self.squareIsEmpty(row,col):#if the board has empty, the board is not full.
                    return False
        return True
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) of their
        mark (three Xs for Player 1, three Os for Player 2), or 3 draws. That line
        can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # TO DO: delete pass (and this comment) and complete method
        

        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == "X" or self.board[row][0] == self.board[row][1] == self.board[row][2] == "O" or self.board[row][0] == self.board[row][1] == self.board[row][2] == "D":#determine the row
                return True

            
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == "X" or self.board[0][col] == self.board[1][col] == self.board[2][col] == "O" or self.board[0][col] == self.board[1][col] == self.board[2][col] == "D":#determine the column
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == "X" or self.board[0][0] == self.board[1][1] == self.board[2][2] == "O" or self.board[0][0] == self.board[1][1] == self.board[2][2] == "D":#determine the right slash
            return True
        elif self.board[2][0] == self.board[1][1] == self.board[0][2] == "X" or self.board[2][0] == self.board[1][1] == self.board[0][2] == "O" or self.board[2][0] == self.board[1][1] == self.board[0][2] == "D":#determine the tleft slash
            return True
        else:
            return False   
    
    def getLocalBoard(self, row, col):
        '''
        Returns the instance of the empty local board at the specified row, col 
        location (i.e. either ClassicTicTacToe or NumTicTacToe).
        Inputs:
           row (int) - row index of square
           col (int) - column index of square
        Returns: instance of appropriate empty local board if un-played; 
                 None if local board has already been played
        '''
        # TO DO: delete pass (and this comment) and complete method
        if self.board[row][col] == "n":#choose the localboard
            Class = NumTicTacToe()
        elif self.board[row][col] == 'c':
            Class = ClassicTicTacToe()
        else:
            return

        return Class
if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required
    
    # start by creating empty board and checking the contents of the board attribute
    localboard = NumTicTacToe()
    print('Contents of board attribute when object first created:')
    print(localboard.board)
    
    # does the empty board display properly?
    localboard.drawBoard()
    # assign a number to an empty square and display
    print('assign a number 5 to (1, 0)')
    localboard.update(1, 0, 5)
    localboard.drawBoard()
    # try to assign a number to a non-empty square. What happens?
    print('assign a number 1 to (1, 0)')
    localboard.update(1, 1, 7)
    localboard.drawBoard()
    # check if the board has a winner. Should there be a winner after only 1 entry?
    print('Is Winner?', localboard.isWinner())
    # check if the board is full. Should it be full after only 1 entry?
    print('Is Full?', localboard.boardFull())
    # add values to the board so that any line adds up to 15. Display
    localboard.update(0, 0, 5)
    localboard.update(2, 2, 3)
    localboard.update(1, 0, 1)
    localboard.update(2, 0, 2)
    localboard.update(0, 1, 3)
    localboard.update(2, 1, 4)
    localboard.update(0, 2, 5)
    localboard.update(1, 2, 6)
    localboard.drawBoard()
    # check if the board has a winner
    print('Is there a Winner?', localboard.isWinner())
    # check if the board is full
    print('Is the board Full?', localboard.boardFull())
   
    
    
    mark1 = "X"
    mark2 = "O"
    localboard = ClassicTicTacToe()
    print('Contents of board attribute when object first created:')
    print(localboard.board)
    
    # does the empty board display properly?
    localboard.drawBoard()
    # assign a number to an empty square and display
    print('assign a "X" to (1, 1)')
    localboard.update(1, 1, str(mark1))
    localboard.drawBoard()
    # try to assign a number to a non-empty square. What happens?
    print('assign a "O" to (1, 1)')
    localboard.update(1, 0, str(mark2))
    localboard.drawBoard()
    
    localboard.update(0, 0, str(mark1))
    localboard.update(2, 2, str(mark1))
    localboard.update(1, 0, str(mark1))
    localboard.update(2, 0, str(mark1))
    localboard.update(0, 1, str(mark1))
    localboard.update(2, 1, str(mark1))
    localboard.update(0, 2, str(mark1))
    localboard.update(1, 2, str(mark1))
    localboard.drawBoard()
    # check if the board has a winner
    print('Is there a Winner?', localboard.isWinner())
    # check if the board is full
    print('Is the board Full?', localboard.boardFull())
    
    
    

    mark1 = "X"
    mark2 = "O"
    configFile = ['c', 'c', 'n'],['c', 'n', 'c'],['n', 'c', 'n']
    localboard = MetaTicTacToe(configFile)

  
    
    print('Contents of board attribute when object first created:')
    print(localboard.board)
    # does the empty board display properly?
    localboard.drawBoard()
    # assign a number to an empty square and display
    print('assign a "X" to (1, 1)')
    localboard.update(1, 1, str(mark1))
    localboard.drawBoard()
    # try to assign a number to a non-empty square. What happens?
    print('assign a "O" to (1, 1)')
    localboard.update(1, 0, str(mark2))
    localboard.drawBoard()
    
    
    localboard.update(0, 0, str(mark1))
    localboard.update(2, 2, str(mark1))
    localboard.update(1, 0, str(mark1))
    localboard.update(2, 0, str(mark1))
    localboard.update(0, 1, str(mark1))
    localboard.update(2, 1, str(mark1))
    localboard.update(2, 0, str(mark1))
    localboard.update(1, 2, str(mark1))
    
    localboard.drawBoard()
    # check if the board has a winner
    print('Is there a Winner?', localboard.isWinner())
    # check if the board is full
    print('Is the board Full?', localboard.boardFull())
   

    pass
    