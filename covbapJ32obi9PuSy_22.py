
def diamond_arrays(x):
  if x == 1:
    return [[1]]
  output = []
  for i in range(1, x + 1):
    row = []
    while len(row) < i:
      row.append(i)
    output.append(row)
  for i in range(x-1, 0, -1):
    row = []
    while len(row) < i:
      row.append(i)
    output.append(row)
  return output

