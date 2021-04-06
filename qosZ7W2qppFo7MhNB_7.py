
def hex_distance(grid):
  x1, y1 = None, None
  for r,row in enumerate(grid):
    for c,char in enumerate(row):
      if char == 'x':
        if x1 != None:
          x2, y2 = (r+c) // 2, r
          if (x1-x2)*(y1-y2) < 0:
            return abs(x1-x2)+abs(y1-y2)
          return max(abs(x1-x2), abs(y1-y2))
        else:
          x1, y1 = (r+c) // 2, r

