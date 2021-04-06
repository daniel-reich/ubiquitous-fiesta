
def rotate_matrix(mat, turns=1):
  
  class Matrix:
  
    def __init__(self, mat):
      self.mat = mat
      
      self.rows = [m for m in self.mat]
      self.cols = []
      
      for c in range(len(self.mat[0])):
        col = []
        for row in self.rows:
          col.append(row[c])
        self.cols.append(col)
    
    def turn(self):
      
      new_mat = [list(reversed(c)) for c in self.cols]
      
      self.mat = new_mat
      
      self.rows = [m for m in self.mat]
      self.cols = []
      
      for c in range(len(self.mat[0])):
        col = []
        for row in self.rows:
          col.append(row[c])
        self.cols.append(col)
      
      return True
    
    def right_turn(self, times):
      for n in range(times):
        self.turn()
      return self.mat
    
    def left_turn(self, times):
      t = abs(times) % 4
      
      if t == 0:
        pass
      elif t == 1:
        return self.right_turn(3)
      elif t == 2:
        return self.right_turn(2)
      elif t == 3:
        return self.right_turn(1)
      else:
        return 'Turn Error: times = {}, t = {}'.format(times,t)
  
  m = Matrix(mat)
  
  if turns >= 0:
    return m.right_turn(turns)
  else:
    return m.left_turn(turns)

