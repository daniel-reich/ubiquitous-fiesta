
import numpy as np
class Sudoku:
  def __init__(self,string):
    self.b = np.array([int(s) for s in string]).reshape(9,9)
    self.board = [list(low) for low in self.b]
  def get_row(self,index):
    return list(self.b[index])
  
  def get_col(self,index):
    return list(self.b[:,index].reshape(-1))
    
  def get_sqr(self,n,m=-1):
    Sqrlist =[np.hsplit(arr,3) for arr in np.split(self.b,3)]
    if m == -1:
      n,m = n//3,n%3
    else:
      n,m = n//3,m//3
    return list(Sqrlist[n][m].reshape(-1))

