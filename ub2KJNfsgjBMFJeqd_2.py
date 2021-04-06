
import random
​
class Game:
    def __init__(self,rows=14,cols=18,mines=40):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[Cell(r,c) for c in range(self.cols)] for r in range(self.rows)]
        
        n = 0
        while n < self.mines:
            r,c = random.randint(0,self.rows-1),random.randint(0,self.cols-1)
            if not self.board[r][c].mine:
                self.board[r][c].mine = True
                n += 1
​
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if 0 <= r+x < self.rows and 0 <= c+y < self.cols:
                            self.board[r+x][c+y].neighbors += 1
                self.board[r][c].neighbors -= 1
            
class Cell:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.mine = False
        self.flag = False
        self.open = False
        self.neighbors = 0

