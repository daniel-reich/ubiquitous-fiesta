
def build_staircase(height, block):
  stair = []
  for i in range(height):
    l = []
    for j in range(height):
      l.append("_")
    stair.append(l)
  print("Before: " + str(stair))
  for i in range(1, height + 1):
    for j in range(i):
      print(i, j)
      stair[i- 1][j] = block
  print("After: " + str(stair))
  return(stair)

