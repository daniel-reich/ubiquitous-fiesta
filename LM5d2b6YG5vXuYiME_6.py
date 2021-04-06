
def can_enter_cave(lst):
  m = len(lst)
  n = len(lst[0])
  queue = []
  
  for i in range(m):
    if lst[i][0] == 0:
      lst[i][0] = 0
      queue.append((i,0))
  
  while len(queue)>0:
    x,y = queue.pop()
    if y == n-1:
      return True
    
    lst[x][y] = 1
    if x<m-1 and lst[x+1][y] == 0:
      queue.append((x+1,y))
    if x>0 and lst[x-1][y] == 0:
      queue.append((x-1,y))
    if y<n-1 and lst[x][y+1] == 0:
      queue.append((x,y+1))
    if y>0 and lst[x][y-1] == 0:
      queue.append((x,y-1))
    
  return False

