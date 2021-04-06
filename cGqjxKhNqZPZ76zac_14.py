
def fire(matrix, coordinates):
  return "splash" if matrix[ord(coordinates[0])-65][int(coordinates[1])-1]=="." else "BOOM"

