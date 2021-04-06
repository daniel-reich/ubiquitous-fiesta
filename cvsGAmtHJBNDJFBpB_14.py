
def can_traverse(x):
  r = len(x)-1
  c = 0
  while c != len(x[0])-1:
    print(c,r)
    # if on bottom
    if r == len(x)-1:
      if x[r][c+1] == 0: c = c+1
      elif x[r][c+1] == 1 and x[r-1][c+1] == 0: r, c = r - 1, c + 1
      else: break
    # if on next up
    elif r == len(x)-2:
      if x[r+1][c+1] == 0: c, r = c+1, r+1
      elif x[r][c+1] == 1 and x[r-1][c+1] == 0: r, c = r-1, c+1
      elif x[r][c+1] == 0 and x[r+1][c+1] == 1: c += 1
      else: break
    # if on top
    elif r == 0:
      if x[r+1][c+1] == 0 and x[r+2][c+1] == 1: c, r = c+1, r+1
      elif x[r][c+1] == 0 and x[r+1][c+1] == 1: c += 1
      else: break
    # else anywhere else
    else:
      if x[r+1][c+1] == 0 and x[r+2][c+1] == 1: c, r = c+1, r+1
      elif x[r][c+1] == 0 and x[r+1][c+1] == 1: c += 1
      elif x[r][c+1] == 1 and x[r-1][c+1] == 0: r, c = r-1, c+1
      else: break
  if c == len(x[0])-1: return True
  return False

