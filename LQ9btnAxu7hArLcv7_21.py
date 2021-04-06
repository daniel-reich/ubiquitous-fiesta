
def diagonalize(n, d):
  matrix = []
  for row in range(n):
    matrix.append([])
  if d[0] == 'u' or d[0] == 'U':
    for i in range(n):
      for number in range(n):
        matrix[i].append(i + number)
      if d[1] == 'r' or d[1] == 'R':
        matrix[i].reverse()
  elif d[0] == 'l' or d[0] == 'L':
    count = 0
    for i in range(n - 1, -1, -1):
      for number in range(n):
        matrix[i].append(number + count)
      if d[1] == 'r' or d[1] == 'R':
        matrix[i].reverse()
      count += 1
  return matrix

