
class Cell:
    def __init__(self, row=None, col=None):
        self.row=row
        self.col = col
        self.mine = False
        self.flag = False
        self.open = False
        self.neighbors = 0
​
class Game:
    def __init__(self, rows=14, cols=18, mines=40):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = []
        import random
        for i in range(self.rows):
            r = []
            for j in range(self.cols):
                c = Cell(i,j)
                r.append(c)
            self.board.append(r)
        minecount = 0
        while minecount < self.mines:
            i = random.randint(0, self.rows-1)
            j = random.randint(0, self.cols-1)
            if self.board[i][j].mine == False:
                self.board[i][j].mine = True
                minecount += 1
        for i in range(self.rows):
            for j in range(self.cols):
                nbr = 0
                for m in [-1,0,1]:
                    for n in [-1,0,1]:
                        if i+m == i and j+n == j:
                            nbr += 0
                        elif i+m<0 or j+n<0:
                            nbr += 0
                        elif i+m>self.rows-1 or j+n>self.cols-1:
                            nbr += 0
                        else:
                            nbr += self.board[i+m][j+n].mine
                self.board[i][j].neighbors = nbr

