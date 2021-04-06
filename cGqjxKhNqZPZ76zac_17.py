
def fire(matrix, coordinates):
  coord = coordinates[0]
  y = int(coordinates[1])
  if coord == 'A':
    x = 0
  elif coord == 'B':
    x = 1
  elif coord == 'C':
    x = 2
  elif coord == 'D':
    x = 3
  elif coord == 'E':
    x = 4
  if matrix[x][y-1] == '.': return 'splash'
  else: return 'BOOM'

