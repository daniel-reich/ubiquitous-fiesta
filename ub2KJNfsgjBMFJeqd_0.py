
import random
​
class Game:
    
    def __init__(self, rows=14, cols=18, mines=40):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[Cell(r, c, False, False, False, 0) for c in range(cols)] for r in range(rows)]
        
        for pos in random.sample(range(rows*cols), mines):
            self.board[pos//cols][pos%cols].mine = True
            
        for r in range(rows):
            for c in range(cols):
                total = 0
                for i, j in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                    if 0 <= r+i < rows and 0 <= c+j < cols and self.board[r+i][c+j].mine:
                        total += 1
                self.board[r][c].neighbors = total
​
class Cell:
    
    def __init__(self, row, col, mine, flag, open, neighbors):
        self.row = row
        self.col = col
        self.mine = mine
        self.flag = flag
        self.open = open
        self.neighbors = neighbors

