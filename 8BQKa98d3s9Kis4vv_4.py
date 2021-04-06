
def final(rows, columns, instructions):
  m = []
  for row in range(rows):
    m.append([0] * columns)
  for s in instructions:
    if s[1] == 'r':
      row = int(s[0])
      for i in range(columns):
        m[row][i] += 1
    else:
      column = int(s[0])
      for i in range(rows):
        m[i][column] += 1
  
  return m

