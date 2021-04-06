
def can_exit(lst):
  m = len(lst[0])
  n = len(lst)
  alreadyPassed = [[0 for i in range(m)] for j in range(n)]
  
  def check(x,y,dx,dy):
    if x+dx < n and x+dx >= 0 and y+dy < m and y+dy >= 0:
      if not alreadyPassed[x+dx][y+dy]:
        return lst[x+dx][y+dy] == 0
    return False
  
  def propagate(x, y):
    alreadyPassed[x][y] = 1
    if check(x,y,1,0):
      propagate(x+1,y)
    if check(x,y,-1,0):
      propagate(x-1,y)
    if check(x,y,0,1):
      propagate(x,y+1)
    if check(x,y,0,-1):
      propagate(x,y-1)
  
  propagate(0,0)
  return alreadyPassed[n-1][m-1]

