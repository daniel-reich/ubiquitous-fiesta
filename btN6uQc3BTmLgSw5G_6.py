
def spiral_matrix(side, string):
  matrix = [['+' for j in range(side)] for i in range(side)]
  if side % 2 == 0:
    r,c = side//2 - 1, side//2 - 1
  else:
    r,c = side//2, side//2
  matrix[r][c] = string[0]
  total = 0
  start = 0
  directs = ['R','D','L','U','R']
  d = 'U'
  if len(string) > side * side:
    string = string[:side*side]
  for i in range(1,len(string)):
    if start == total:
      d = directs[directs.index(d)+1]
      start = 0
      if d == 'L' or d == 'R':
        total += 1
    if d == 'R':
      c += 1
    elif d == 'D':
      r += 1
    elif d == 'L':
      c -= 1
    else:
      r -= 1
    matrix[r][c] = string[i]
    start +=1
  return matrix

