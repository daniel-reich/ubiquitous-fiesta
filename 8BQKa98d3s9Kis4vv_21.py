
def final(r, c, i):
  matrix = [[0 for cn in range(c)] for rn in range(r)]
  for op in i:
    if 'r' in op:
      row = int(op.split('r')[0])
      for n in range(c):
        matrix[row][n]+=1
    elif 'c' in op:
      col = int(op.split('c')[0])
      for n in range(r):
        matrix[n][col]+=1
  return matrix

