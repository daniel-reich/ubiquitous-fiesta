
def rotate_matrix(mat, turns = 1):
  matrix, imax, jmax = convert_list(mat)
  for _ in range(turns%4):
    matrix, imax, jmax = rotate_one(matrix, imax, jmax)
  return convert_matrix(matrix)
​
def convert_list(mat):
  matrix = {(i,j) : char for j, line in enumerate(mat) for i, char in enumerate(line)}
  imax = max([k[0] for k in matrix.keys()])
  jmax = max([k[1] for k in matrix.keys()])
  return matrix, imax, jmax 
def rotate_one(matrix, imax, jmax):
  return {(jmax -j,i) : matrix[(i,j)] for i in range(imax+1) for j in range(jmax+1)} , jmax, imax
def convert_matrix(matrix):
  imax = max([k[0] for k in matrix.keys()])
  jmax = max([k[1] for k in matrix.keys()])
  return [[matrix[(i,j)] for i in range(imax+1)]for j in range(jmax+1)]

