
def spiral_order(matrix):
  if len(matrix) == 1:
    return matrix[0][:-1]
  else:
    print(matrix, len(matrix), 'l.5')
    spiral = matrix[0]
    for n in range(1, len(matrix)-1):
      try:
        spiral.append(matrix[n][-1])
      except IndexError:
        print(n, 'l.10')
    spiral += list(reversed(matrix[-1]))
    for n in reversed(range(1, len(matrix) - 1)):
      try:
        spiral.append(matrix[n][0])
      except IndexError:
        print(n, 'l.16')
    nl = []
    for r in range(1, len(matrix)-1):
      nr = []
      for c in range(1, len(matrix[0])-2):
        try:
          nr.append(matrix[r][c])
        except IndexError:
          print(r, c, 'l.24')
      nl.append(nr)
    print(nl, 'l.26')
    return spiral + spiral_order(nl)

