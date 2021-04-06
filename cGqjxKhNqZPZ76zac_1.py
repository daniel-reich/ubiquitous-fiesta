
def fire(matrix, coordinates):
  x, y = coordinates
  return 'BOOM' if matrix[ord(x) - 65][int(y) - 1] == '*' else 'splash'

