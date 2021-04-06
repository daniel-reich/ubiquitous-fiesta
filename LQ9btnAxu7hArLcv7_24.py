
def diagonalize(n, d):
  lst = [[0] * n for i in range(n)]
  up = 1; right = 1
  if d == "ur":
    right = -1
  elif d == "ll":
    up = -1
  elif d == "lr" :
    up = -1
    right = -1
  
  for x in range(0, n) :
    for y in range(0, n) :
      lst[x][y] = x+y
  
  if(up == -1) :
    lst.reverse()
  if(right == -1) :
    for x in range(n) :
      lst[x].reverse()
  return lst

