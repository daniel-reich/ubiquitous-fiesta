
class Multiplication_Table:
  class Row:
​
    def __init__(self, rval, size):
      self.rval = rval
      self.size = size
​
      self.row = [rval * n for n in range(1, size + 1)]
  
  def __init__(self, val):
    self.val = val
​
    self.rows = {n:Multiplication_Table.Row(n, val) for n in range(1, val+1)}
  
  def display(self):
    tr = []
    for n in sorted(self.rows.keys()):
      tr.append(self.rows[n].row)
    return tr
​
def multiplication_table(n):
  table = Multiplication_Table(n)
  return table.display()

