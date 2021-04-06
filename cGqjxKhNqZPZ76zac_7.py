
def fire(matrix, coordinates):
  row = ['A','B','C','D','E']
  if matrix[row.index(coordinates[0])][int(coordinates[1])-1] == '.':
    return 'splash'
  return 'BOOM'

