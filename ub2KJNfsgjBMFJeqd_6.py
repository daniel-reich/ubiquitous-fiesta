
import random
​
class Game:
​
    def __init__(self, rows=14, columns=18, mines=40):
        self.rows = rows
        self.cols = columns
        self.mines = mines
        self.board = []
        # determine mine positions randomly:
        mine_pos = []
        while len(mine_pos) < mines:
            r, c = random.randint(0, rows - 1), random.randint(0, columns - 1)
            while (r, c) in mine_pos:
                r, c = random.randint(0, rows - 1), random.randint(0, columns - 1)
            mine_pos.append((r, c))
        # now construct board:
        for r in range(rows):
            row = []
            for c in range(columns):
                cell = Cell(r, c, (r, c) in mine_pos)
                row.append(cell)
                for r2 in range(r - 1, r + 2):
                    for c2 in range(c - 1, c + 2):
                        if (r2, c2) != (r, c) and (r2, c2) in mine_pos:
                            cell.addMineNeighbor()
            self.board.append(row[:])
  
class Cell:
​
    def __init__(self, row, col, mine):
        self.row = row
        self.col = col
        self.mine = mine
        self.neighbors = 0
        self.flag = False
        self.open = False
​
    def addMineNeighbor(self):
        self.neighbors += 1

