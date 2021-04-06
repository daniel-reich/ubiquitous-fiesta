
import random
class Game:
  def __init__(self, rows = 14, cols = 18, mines = 40):
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.mine_dist = [1]*mines+[0]*(rows*cols-mines)
    random.seed(3)
    random.shuffle(self.mine_dist)
    self.mine_board = [self.mine_dist[row*cols:(row+1)*cols] for row in range(rows)]
    self.padded = [[0]*(cols+2)]+[[0] + row + [0] for row in self.mine_board]+[[0]*(cols+2)]
    self.neighbor_board = []
    for i in range(1,len(self.padded)-1):
      row = []
      for j in range(1,len(self.padded[i])-1):
        sum = 0
        for (u, v) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
          sum += self.padded[i+u][j+v]
        row.append(sum)
      self.neighbor_board.append(row)
    self.board = [[Cell(row,col,self.mine_board[row][col],self.neighbor_board[row][col]) for col in range(cols)] for row in range(rows)]
class Cell:
  def __init__(self, row, col, mine, neighbors):
    self.row = row
    self.col = col
    self.mine = mine
    self.flag = False
    self.open = False
    self.neighbors = neighbors

