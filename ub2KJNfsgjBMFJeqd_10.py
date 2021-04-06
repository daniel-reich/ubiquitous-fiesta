
from random import shuffle
import numpy as np
class Game:
  def __init__(self, rows=14, cols=18, mines=40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.create_minefield()
    self.create_neighborsfield()
    self.create_board()   
  
  def create_minefield(self):
    self.minefield = [True for x in range(self.mines)] + [False for x in range((self.rows*self.cols)-self.mines)]
    shuffle(self.minefield)
    self.minefield = np.array(self.minefield).reshape(self.rows,self.cols)
​
  def create_neighborsfield(self):
    self.neighborsfield = np.zeros((self.rows,self.cols))
    for c in range(self.cols):
      for r in range(self.rows):      
        n = 1
        r1 = max(r-n,0)
        r2 = min(r+n+1, self.rows)
        c1 = max(c-1,0)
        c2 = min(c+n+1, self.cols)
        self.neighborsfield[r,c] = self.minefield[r1:r2,c1:c2].sum()
​
        if self.minefield[r,c] == 1:
          self.neighborsfield[r,c] -= 1
​
  def create_board(self):
    self.board = [[Cell(r,c,self.minefield[r,c],self.neighborsfield[r,c]) for c in range(self.cols)] for r in range(self.rows)]
​
class Cell:
  def __init__(self, row, col, mine, neighbors):
    self.row = row
    self.col = col
    self.mine = mine
    self.flag = False
    self.open = False
    self.neighbors = neighbors

