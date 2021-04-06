
def id_mtrx(n):
  if type(n) != int:
    return "Error"
  matrix = []
  neg = n
  if n < 0:
    n *= -1
  for each in range(n):
    new = []
    for _ in range(n):
      new.append(0)
    new[each] = 1
    matrix.append(new)
  if neg < 0:
    for each in range(len(matrix)):
      matrix[each].reverse()
  return matrix

