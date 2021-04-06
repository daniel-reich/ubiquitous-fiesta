
def odd_square_patch(lst):
  maxpatch = 0
  if len(lst[0]) == 0:
    return maxpatch
  for y in range(len(lst)):
    for x in range(len(lst)):
      if lst[y][x]%2 == 1:
        for z in range(len(lst[y])-x+1):
          if y+z <= len(lst):
            if all([all([lst[i][j]%2 == 1 for j in range(x,x+z)]) for i in range(y,y+z)]):
              maxpatch = max(maxpatch,z)
  return maxpatch

