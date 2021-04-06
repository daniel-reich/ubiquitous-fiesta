
def build_staircase(height, block):
  res = [['_']*height for _ in range(height)]
  for i in range(height):
    for j in range(i+1):
      res[i][j] = block
  return res

