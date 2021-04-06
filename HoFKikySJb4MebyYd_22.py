
class Entry:
  def __init__(self,lst):
    self.lst = lst
    self.rows = [row for row in lst]
    self.cols = [[lst[i][j] for i in range(0,len(lst))] for j in range(0,len(lst[0]))]
  def sums(self,i,j):
    return sum(self.rows[i]) + sum(self.cols[j]) - (2 * self.lst[i][j])
def transform_matrix(lst):
  matrix = Entry(lst)
  transform = [[matrix.sums(i,j) for j in range(0,len(lst[0]))] for i in range(0,len(lst))]
  return transform

