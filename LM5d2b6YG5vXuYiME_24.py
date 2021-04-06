
def can_enter_cave(x):
  cave,complete = x.copy(),0
  for r in range (len(cave)):
    if cave[r][0]==0:
      cave[r][0] = 2
  while complete != 1:
    complete = 1
    for c in range (1,len(cave[0])):
      for r in range (len(cave)):
        if cave[r][c]==0:
          if cave[r][c-1]==2:
            cave[r][c] = 2
            complete = 0
          elif c < len(cave[0])-1:
            if cave[r][c+1]==2:
              cave[r][c] = 2
              complete = 0
          if r > 0:
            if cave[r-1][c]==2:
              cave[r][c] = 2
              complete = 0
          if r < len(cave)-1:
            if cave[r+1][c]==2:
              cave[r][c] = 2
              complete = 0
    for r in range (len(cave)):
      if cave[r][-1]==2:
        return True
  return False

