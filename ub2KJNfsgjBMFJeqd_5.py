
from random import randrange
class Game:
  def __init__(self, rows = 14, cols = 18, mines = 40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.board = []
    #Initialize board
    for i in range(self.rows):
      self.board.append([])
      for j in range(self.cols):
        self.board[i].append(Cell(i,j))
    #Randomize Mines
    while(mines):
      mineRow, mineCol = randrange(0,rows), randrange(0,cols)
      if not self.board[mineRow][mineCol].mine:
        self.board[mineRow][mineCol].mine = True
        mines -= 1
    #Update neighbors
    for i in range(self.rows):
      for j in range(self.cols):
        if self.board[i][j].mine:
          for k in range(max(0,i-1),min(self.rows,i+2)):
            for l in range(max(0,j-1),min(self.cols,j+2)):
              if not (i==k and j==l):
                self.board[k][l].neighbors += 1
class Cell:
  def __init__(self,row,col):
    self.row = row
    self.col = col
    self.mine = False
    self.flag = False
    self.open = False
    self.neighbors = 0
  def __repr__(self):
    return '*' if self.mine else '_'

