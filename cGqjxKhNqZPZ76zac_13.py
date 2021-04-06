
def fire(matrix, coordinates):
  trans = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4}
  x = trans[coordinates[0]]
  y = int(coordinates[1])-1
  if matrix[x][y] == "*":
    return 'BOOM'
  return "splash"

