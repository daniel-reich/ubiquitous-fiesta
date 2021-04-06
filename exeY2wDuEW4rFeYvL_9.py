
def ordered_matrix(height, width):
  matrix = []
  Neo = 0
  TAA = 0 #(Thomas A. Anderson)
  #Get it?
  Number = 1
  while(Neo < height):
    matrix.append([])
    Neo = Neo + 1
  Neo = 0
  while(Neo < height):
    while(TAA < width):
      matrix[Neo].append(Number)
      TAA = TAA + 1
      Number = Number + 1
    TAA = 0
    Neo = Neo + 1
  return(matrix)
  #Code By Cool Programmer

