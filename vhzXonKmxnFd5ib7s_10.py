
def matrix_multiply(a, b):
  rowA = len(a)
  rowB = len(b)
  colA = len(a[0])
  colB = len(b[0])
​
  if colA != rowB:
    return "invalid"
​
  result = []
  for i in range(rowA):
    row = []
    for j in range(colB):
      value = 0
      for k in range(colA):
        value += a[i][k] * b[k][j]
      row.append(value)
    result.append(row)
​
  return result

