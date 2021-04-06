
class Game:
    def __init__(self, row=14, columns=18, mines=40):
        self.rows = row
        self.cols = columns
        self.mines = mines
        self.board = [[Cell(x, y) for y in range(columns)]for x in range(row)]
        a = 0
        for x in self.board:
            for y in x:
                if a != self.mines:
                    y.mine = True
                    a += 1
                else:
                    break
        # update neighbors
        moves = [(1,0), (0,1), (-1,0), (0,-1), (-1, -1), (1,1), (-1, 1), (1, -1)]
        for x in range(self.rows):
            for y in range(self.cols):
                self.board[x][y].neighbors = sum([self.board[x+a][y+b].mine == True for a, b in moves if 0 <= a+x < self.rows and 0 <= b+y < self.cols])
​
class Cell:
    def __init__(self, row, col, mine=False, flag=False, open=False, neighbors=0):
        self.row = row
        self.col = col
        self.mine =  mine
        self.flag = flag
        self.open = open
        self.neighbors = neighbors

