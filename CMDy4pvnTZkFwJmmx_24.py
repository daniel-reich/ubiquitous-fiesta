
class Sudoku:
  def __init__(self,string):
    self.board = []
    for i in range(0,len(string),9):
      self.board.append([int(x) for x in string[i:i+9]])
  
  def get_row(self,row):
    return self.board[row]
  
  def get_col(self,col):
    columns = [[i[j] for i in self.board] for j in range(9)]
    return columns[col]
    
  def get_sqr(self,n,m=-1):
    if m<0:
      if n<3:
        rows = [0,1,2]
      elif 3<=n<6:
        rows = [3,4,5]
      else:
        rows = [6,7,8]
      if n%3==0:
        cols = [0,1,2]
      elif n%3==1:
        cols = [3,4,5]
      else:
        cols = [6,7,8]
      lst = []
      for r in rows:
        for c in cols:
          lst.append(self.board[r][c])
      return lst
    else:
      if n<3:
        return self.get_sqr(0) if m<3 else self.get_sqr(1) if 3<=m<6 else self.get_sqr(2)
      elif 3<=n<6:
        return self.get_sqr(3) if m<3 else self.get_sqr(4) if 3<=m<6 else self.get_sqr(5)
      else:
        return self.get_sqr(6) if m<3 else self.get_sqr(7) if 3<=m<6 else self.get_sqr(8)

