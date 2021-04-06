
def id_mtrx(n):
  try:
    matrix = [[0 for x in range (abs(n))] for y in range(abs(n))]
    for i in range(abs(n)):
      matrix[i][i] = 1
    if n < 0:
      matrix.reverse()
    return matrix
  except:
    return "Error"

