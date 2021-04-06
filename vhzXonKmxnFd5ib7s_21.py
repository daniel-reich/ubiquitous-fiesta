
class Matrix:
  
  def __init__(self, matrix):
    self.mtx = matrix
    
    self.cols = []
    
    for c in range(len(self.mtx[0])):
      col = [self.mtx[r][c] for r in range(len(self.mtx))]
      self.cols.append(col)
  
  def multiply(self, other):
    
    if len(self.cols) != len(other.mtx):
      return 'invalid'
    
    nm = []
    
    for n in range(len(self.mtx)):
      sr = self.mtx[n]
      row = []
      for c in range(len(other.cols)):
        oc = other.cols[c]
        #print(sr, oc, len(sr), len(oc))
        products = [sr[i] * oc[i] for i in range(len(sr))]
        row.append(sum(products))
      nm.append(row)
    
    return Matrix(nm)
  
  def display(self):
    return self.mtx
      
      
      
def matrix_multiply(a, b):
  
  m1 = Matrix(a)
  m2 = Matrix(b)
  
  m3 = m1.multiply(m2)
  #print(m3)
  try:
    return m3.display()
  except AttributeError:
    return m3

