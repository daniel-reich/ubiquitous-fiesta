
def final(rows, columns, operations):
  matrix = [[0 for _ in range(columns)] for _ in range(rows)]
  for operation in operations:
    i = int(operation[0])
    axis = operation[1]
    if axis == 'r':
      for y in range(columns):
        matrix[i][y] += 1
    elif axis == 'c':
      for x in range(rows):
        matrix[x][i] += 1
  return matrix

