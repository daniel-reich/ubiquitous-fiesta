
class Triangle:
  
  def __init__(self, triangle = []):
    self.tri = triangle
    self.last_num = 0
    self.next_row_size = 1
  
  def add_row(self):
    row = []
    while len(row) < self.next_row_size:
      row.append(self.last_num + 1)
      self.last_num += 1
    self.tri.append(row)
    self.next_row_size += 1
    return True
  
  def up_to(self, goal):
    tr = []
    
    for row in self.tri:
      tr.append(row)
      if goal in row:
        break
    
    return tr
  
  def n_row(self, row):
    return self.tri[:row]
  
  def increase_to(self, size):
    while len(self.tri) < size:
      self.add_row()
    return True
​
floyd_triangle = Triangle()
​
floyd_triangle.increase_to(11)
​
def floyd(up_to = None, n_row = None):
  if up_to == None:
    return floyd_triangle.n_row(n_row)
  else:
    return floyd_triangle.up_to(up_to)

