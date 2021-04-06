
from random import randint
  
class Game:
  def __init__(self, rows=14, cols=18, mines=40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.board = [[Cell(r, c) for c in range(cols)] for r in range(rows)]
    while mines > 0:
      cell = self.board[randint(0, rows-1)][randint(0, cols-1)]
      if not cell.mine:
        cell.mine = True
        mines -= 1
    for r in range(rows): 
      for c in range(cols):
        for nrc in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
          nr, nc = r + nrc[0], c + nrc[1]
          if 0 <= nr < rows and 0 <= nc < cols and self.board[nr][nc].mine:
            self.board[r][c].neighbors += 1
​
​
class Cell:
  def __init__(self, row, col, isMine=False):
    self.row = row
    self.col = col
    self.mine = isMine
    self.flag = False
    self.open = False
    self.neighbors = 0

