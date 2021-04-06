
def diagonalize(n, d):
  matrix = []
  for i in range(n):
    row = []
    if(d[1] == 'l'):
      for j in range(n):
        row.append(j + i)
    else:
      for j in range(n):
        row.insert(0, j + i)
    if(d[0] == 'u'):
      matrix.append(row)
    else:
      matrix.insert(0, row)
  return matrix

