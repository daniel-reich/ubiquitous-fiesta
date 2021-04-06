
def fire(matrix, coord):
  return "BOOM" if matrix[ord(coord[0])-65][int(coord[-1])-1] == "*" else "splash"

