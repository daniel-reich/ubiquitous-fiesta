
import random
​
class Game:
    def __init__(self, rows = 14, cols = 18, mines = 40):
        self.rows = rows
        self.cols = cols
        self.mines = mines
​
        self.board = [[Cell(x, y) for y in range(cols)] for x in range(rows)]
​
        c = []
​
        for x in range(rows):
            for y in range(cols):
                c.append([x, y])
​
        random.shuffle(c)
​
        for x in range(mines):
            self.board [c[x][0]][c[x][1]].set_mine(True)
​
        for row in self.board:
            for cell in row:
                cell.set_game(self)
​
    def display(self):
        for x in range(self.rows):
            row = ""
            for y in range(self.cols):
                row += self.board [x][y].get_val() + " "
            print(row)
        
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mine = False
        self.flag = False
        self.open = False
​
        self.neighbors = 0
​
    def set_mine(self, mine):
        self.mine = mine
​
    def set_game(self, game):
        rows = game.rows
        cols = game.cols
​
        for a in range(-1, 2):
            for b in range(-1, 2):
                if not ( a == 0 and b == 0 ):
                    if self.row + a >= 0 and self.row + a < rows:
                        if self.col + b >= 0 and self.col + b < cols:
                            if game.board [self.row+a][self.col+b].mine:
                                self.neighbors += 1
​
    def get_val(self):
        if self.mine:
            return "M"
        else:
            return str(self.neighbors)

