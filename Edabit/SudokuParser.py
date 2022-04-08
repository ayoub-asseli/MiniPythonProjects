"""
Create a class Sudoku that takes a string as an argument. The string will contain the numbers of a regular 9x9 sudoku board left to 
right and top to bottom, with zeros filling up the empty cells.

Attributes
An instance of the class Sudoku will have one attribute:

board: a list representing the board, with sublits for each row, with the numbers as integers. Empty cell represented with 0.
Methods
An instance of the class Sudoku wil have three methods:

get_row(n): will return the row in position n.
get_col(n): will return the column in position n.
get_sqr([n, m]): will return the square in position n if only one argument is given, and the square to which the cell in position (n, m) 
                 belongs to if two arguments are given.
"""



class Sudoku:

    def __init__(self, str2parse):
        self.str2parse = str2parse
        
    def board(self):
        b, l = [], []
        i = 0
        for f in self.str2parse:
            l.append(f)
            i += 1
            if i == 9:
                b.append(l)
                i = 0
                l = []
        return b


    def get_row(self, n):
        return self.board()[n]

    def get_col(self, n):
        board = self.board()
        res = []
        for i in range(len(board)):
            res.append(board[i][n])
        return res

    def get_sqr(self, n, m=None):
        board = self.board()
        w = len(board)
        l1, l2, l3 = [], [], []
        i=0
        L = []
        while i < w:
            for j in range(w):
                if j < 3:
                    l1.append(board[i][j])
                elif j < 6:
                    l2.append(board[i][j])
                else:
                    l3.append(board[i][j])
            i += 1
            if len(l1) == 9:
                L.append(l1)
                L.append(l2)
                L.append(l3)
                l1, l2, l3 = [], [], []
        if m == None:
            return L[n]
        else:
            if m < 3 and n < 3:
                return L[0]
            elif m >= 3 and m < 6 and n < 3:
                return L[1]
            elif m >= 6 and m < 9 and n < 3:
                return L[2]
            elif m < 3 and n >= 3 and n < 6:
                return L[3]
            elif m >= 3 and m < 6 and n >= 3 and n < 6:
                return L[4]
            elif m >= 6 and m < 9 and n >= 3 and n < 6:
                return L[5]
            elif m < 3 and n >= 6 and n < 9:
                return L[6]
            elif m >= 3 and m < 6 and n >= 6 and n < 9:
                return L[7]
            elif m >= 6 and m < 9 and n >= 6 and n < 9:
                return L[8]
           
          
game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")

print(game.board())
#--> 
[['4', '1', '7', '9', '5', '0', '0', '3', '0'], 
['0', '0', '0', '0', '0', '0', '7', '0', '0'], 
['0', '6', '0', '0', '0', '7', '0', '0', '0'], 
['0', '5', '0', '0', '0', '9', '1', '0', '6'], 
['8', '0', '0', '6', '0', '0', '0', '0', '0'], 
['0', '0', '0', '0', '0', '3', '4', '0', '0'], 
['9', '0', '0', '0', '0', '5', '0', '0', '0'], 
['0', '0', '0', '4', '3', '0', '0', '0', '0'], 
['2', '0', '0', '7', '0', '1', '5', '8', '0']]

print(game.get_row(0))
#--> ['4', '1', '7', '9', '5', '0', '0', '3', '0']

print(game.get_col(8))
#--> ['0', '0', '0', '6', '0', '0', '0', '0', '0']

print('\n\n')

print(game.get_sqr(1))
#--> ['9', '5', '0', '0', '0', '0', '0', '0', '7']

print(game.get_sqr(8, 3))
#--> ['0', '0', '5', '4', '3', '0', '7', '0', '1']
