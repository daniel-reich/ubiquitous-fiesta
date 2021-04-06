
def fire(matrix, coordinates):
  return ['splash','BOOM'][matrix[ord(coordinates[0])-65][int(coordinates[1])-1] == '*']

