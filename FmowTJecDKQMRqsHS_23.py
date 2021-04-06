
def crop_hydrated(field):
  for i in range(len(field)):
    for j in range(len(field[i])):
      if field[i][j] != 'w':
        c = 0
        adj = ((1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1))
        for x, y in adj:
          try:
            if i+x > -1 and j+y > -1:
              if field[i+x][j+y] == 'w':
                c += 1
                break
          except:
            pass
        if not c:
          return False
  return True

