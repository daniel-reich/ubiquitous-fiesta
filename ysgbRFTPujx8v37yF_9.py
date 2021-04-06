
class Triangle:
​
  def __init__(self):
    self.r = {1: [1]}
    self.last_row = 1
    self.last_num = 1
  
  def advance(self):
    
    new_row = self.last_row + 1
    nr = [n for n in range(self.last_num+1, self.last_num + new_row + 1)]
    
    self.last_num = nr[-1]
    self.last_row += 1
    
    self.r[new_row] = nr
    return True
  
  def advance_to_row(self, row_goal):
    while self.last_row < row_goal:
      self.advance()
    return True
  
  def advance_to_num(self, num_goal):
    while self.last_num < num_goal:
      self.advance()
    return True
  
  def search_by_row(self, row):
    return self.r[row]
  
  def search_by_num(self, num):
    return self.r[[k for k in self.r.keys() if num in self.r[k]][0]]
​
t = Triangle()
​
t.advance_to_row(1000)
​
def row_sum(n):
  return sum(t.search_by_row(n))

