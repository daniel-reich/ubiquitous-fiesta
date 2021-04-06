
from random import randint
​
class Game:
  def __init__(self, rows=14, cols=18, mines=40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.board = self.build_board(rows, cols, mines)
​
  def build_board(self, n, m, b):
    #build board
    board = [[Cell(x, y) for y in range(m)] for x in range(n)]
​
    #lay mines
    c = 0
    while c < b:
      i = randint(0,n-1)
      j = randint(0,m-1)
      if board[i][j].mine:
        pass
      else:
        board[i][j].mine = True
        c += 1
​
    #populate neighbors
    for i, row in enumerate(board):
      for j, cell in enumerate(row):
        adj = ((1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1))
        for x, y in adj:
          if i+x >= 0 and j+y >= 0:
            try:
              cell.neighbors += board[i+x][j+y].mine
            except:
              pass
    return board
  
class Cell:
  def __init__(self, x, y):
    self.row = x
    self.col = y
    self.flag = False
    self.open = False
    self.mine = False
    self.neighbors = 0

