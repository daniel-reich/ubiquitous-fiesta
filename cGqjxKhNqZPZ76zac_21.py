
from string import ascii_uppercase as asc
​
def fire(matrix, coordinates):
  x, y = asc.index(coordinates[0]), int(coordinates[1]) - 1
  return 'splash' if matrix[x][y] == '.' else 'BOOM'

