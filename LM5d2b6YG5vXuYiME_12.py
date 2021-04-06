
def can_enter_cave(x):
  start = [0,0]
  for i in range(len(x)-1,-1,-1):
    if x[i][0] == 0:
      start[0] = i
  
  return findpath(x,start,[])
​
def findpath(cave, curr, moves):
​
  h = len(cave)
  w = len(cave[0])
  if curr[1] == w-1: return True
  dirs = [[-1,0], [1,0], [0,-1], [0,1]]
  
  for d in dirs:
    possiblemove = [sum(x) for x in zip(curr, d)]
    #if you havent already been there, and the spot is in range, and it can be moved on
    if possiblemove not in moves and 0 <= curr[0]+d[0] < h and 0 <= curr[1]+d[1] < w and cave[possiblemove[0]][possiblemove[1]] == 0:
      if findpath(cave, possiblemove, moves + [curr]): return True
  return False

