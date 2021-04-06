
def fire(matrix, coordinates):
  square = matrix[ord(coordinates[0]) - 65][int(coordinates[-1]) - 1]
  return "splash" if square == "." else "BOOM"

