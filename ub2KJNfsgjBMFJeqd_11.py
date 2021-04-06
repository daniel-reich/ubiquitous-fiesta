
class Game:
  def __init__(self,rows=14,cols=18,mines=40):
    import random
    self.rows = rows
    self.cols = cols
    self.mines = mines
    self.lis = random.sample(list(range(self.rows*self.cols)),self.mines)
    self.board = []
    for i in range(self.rows):
      self.board.append([])
      for j in range(self.cols):
        if i*self.cols+j in self.lis:
          mine = True
        else:
          mine = False
        self.board[i].append(Cell(self,i,j,mine))
​
class Cell:
  def __init__(self,GameObj,row,col,mine):
    self.row = row
    self.col = col
    self.mine = mine
    self.flag = False
    self.open = False
    neigh_rows = [self.row,self.row+1,self.row-1]
    neigh_cols = [self.col,self.col+1,self.col-1]
    self.neighbors = 0
    for i in neigh_rows:
      for j in neigh_cols:
        if (i,j) != (self.row,self.col) and 0 <= i < GameObj.rows and 0 <= j < GameObj.cols:
          if i*GameObj.cols+j in GameObj.lis:
            self.neighbors += 1

