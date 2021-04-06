
def piece(i,j, material):
  if i<=j:
    return material
  else:
    return '_'
​
​
def build_staircase(height, material):
  staircase = [[piece(i, j, material) for i in range(height)] for j in range(height)]
  return staircase

