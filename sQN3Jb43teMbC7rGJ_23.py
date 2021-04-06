
class Matrix:
  class Space:
​
    def __init__(self, val, row, col):
      self.v = val
      self.r = row
      self.c = col
​
  def __init__(self, mtx):
    self.mtx = mtx
​
    self.spaces = {}
​
    for r in range(len(mtx)):
      for c in range(len(mtx[0])):
        self.spaces['{},{}'.format(r,c)] = Matrix.Space(mtx[r][c], r, c)
  
  def transpose(self):
    nm = []
    
    if len(self.mtx) == len(self.mtx[0]):
      for r in range(len(self.mtx)):
        row = []
        for c in range(len(self.mtx[0])):
          row.append(self.spaces['{},{}'.format(c, r)].v)
        nm.append(row)
    else:
      for c in range(len(self.mtx[0])):
        row = []
        for r in range(len(self.mtx)):
          row.append(self.spaces['{},{}'.format(r, c)].v)
        nm.append(row)
​
    return Matrix(nm)
​
​
def make_transpose(matrix):
​
  matrix = Matrix(matrix)
  transposed = matrix.transpose()
​
  return transposed.mtx

