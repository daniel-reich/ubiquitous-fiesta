
def is_checkerboard(lst):
  for x in range(len(lst)):
    for y in range(len(lst)-1):
      if lst[x][y] != lst[x][y+1]:
        continue
      else:
        return False
  return True

