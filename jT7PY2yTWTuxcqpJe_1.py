
def spiral_order(matrix):
  ans, c = [], 0
  while matrix:
    if c%4==0: new = matrix.pop(0)
    if c%4==1: new = [row.pop(-1) for row in matrix]
    if c%4==2: new = matrix.pop(-1)[::-1]
    if c%4==3: new = [row.pop(0) for row in matrix]
    ans+= new
    c+= 1
  return ans

