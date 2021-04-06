
def complete_square(m):
  row = len(m)
  col = len(m[0])
  if row < col:
    for i in range(col-row):
      m.append(col*[0])
  else:
    for i in range(row):
      m[i] += (row-col) * [0]
  return m

