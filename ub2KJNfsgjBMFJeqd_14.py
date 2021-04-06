
from random import sample
​
​
class Game:
​
  def __init__(self, rows=14, cols=18, mines=40):
    self.rows, self.cols = rows, cols
    self.mines = mines
    self.gen_board()
  
  def gen_board(self):
    self.board = [[Cell(r, c) for c in range(self.cols)] for r in range(self.rows)]
    for cell in sample([i for row in self.board for i in row], self.mines):
      cell.mine = True
    for cell in (i for row in self.board for i in row):
      cell.count_neighbors(self.board)
​
​
class Cell:
​
  def __init__(self, row, col):
    self.row, self.col = row, col
    self.mine = False
    self.flag = False
    self.open = False
    
  def count_neighbors(self, b):
    self.neighbors = 0
    for i in range(-1, 2):
      for j in range(-1, 2):
        nbr, nbc = self.row + i, self.col + j
        if (0 <= nbr < len(b)) and (0 <= nbc < len(b[0])):
          self.neighbors += b[nbr][nbc].mine
    self.neighbors -= self.mine

