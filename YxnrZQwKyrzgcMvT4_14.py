
def rotate_transform(lst, num):
  
  class Matrix:
    
    def __init__(self, mtx):
      self.mtx = mtx
      
      self.cols = []
      
      for n in range(len(self.mtx[0])):
        col = []
        for row in self.mtx:
          col.append(row[n])
        self.cols.append(col)
    
    def rotate_clockwise(self):
      
      self.mtx = [list(reversed(i)) for i in self.cols]
      self.cols = []
      
      for n in range(len(self.mtx[0])):
        col = []
        for row in self.mtx:
          col.append(row[n])
        self.cols.append(col)
        
      return True
    
    def rotate_anticlockwise(self):
      self.mtx = list(reversed(self.cols))
      self.cols = []
      
      for n in range(len(self.mtx[0])):
        col = []
        for row in self.mtx:
          col.append(row[n])
        self.cols.append(col)
    
    def rotate_x_times(self, x):
      if x < 0:
        for n in range(abs(x)):
          self.rotate_anticlockwise()
      else:
        for n in range(x):
          self.rotate_clockwise()
      
      return True
    
  matrix = Matrix(lst)
  matrix.rotate_x_times(num)
  return matrix.mtx

