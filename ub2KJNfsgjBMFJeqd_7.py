
import random
class Game(object):
  def __init__(self, rows = 14, cols = 18, mines = 40):
      self.rows = rows
      self.cols = cols
      self.mines = mines
      #self.board = [[Cell(i, j) for j in range(columns)] for i in range(rows)]
      self.board = [[ "" for j in range(cols)] for i in range(rows)]
      countermines = 0
      for i in range(rows):
          for j in range(cols):
              tmpcell = Cell(i, j)
              if tmpcell.mine:
                  countermines += 1
                  if countermines > self.mines:
                      tmpcell.mine = False
              self.board[i][j] = tmpcell
      for row in self.board:
          for cell in row:
              cell.checkneighbors(self.rows, self.cols, self.board)
​
class Cell(object):
    def __init__(self, row=0, col= 0):
        self.row = row
        self.col = col
        self.mine = True
        self.flag = False
        self.open = False
        self.neighbors = 0
        
    def checkneighbors(self, rows, columns, board):
        neighbors = [[self.row -1, self.col -1],[self.row -1, self.col],[self.row -1, self.col +1],[self.row, self.col -1],[self.row, self.col +1], [self.row +1, self.col -1],[self.row +1, self.col],[self.row +1, self.col +1],]
        nearmines = 0
        for neighbor in neighbors:
            if neighbor[0] >= 0 and neighbor[0] < rows and neighbor[1] >= 0 and neighbor[1] < columns:
                if board[neighbor[0]][neighbor[1]].mine:
                    nearmines += 1
        self.neighbors = nearmines

