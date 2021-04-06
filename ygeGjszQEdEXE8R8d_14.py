
def move(mat):
  matrix = {(i,j): num for j, line in enumerate(mat) for i, num in enumerate(line)}
  imax = max(key[0] for key in matrix.keys())+1
  jmax = max(key[1] for key in matrix.keys())+1
  def movement(string):
    one = [k for k,v in matrix.items() if v == 1][0]  
    if string == "right":
      matrix[one] = 0
      one = ((one[0]+1)%imax, one[1])
      matrix[one] = 1
      return movement
    if string == "left":
      matrix[one] = 0
      one = ((one[0]-1)%imax, one[1])
      matrix[one] = 1
      return movement
    if string == "up":
      matrix[one] = 0
      one = (one[0], (one[1]-1)%jmax)
      matrix[one] = 1
      return movement
    if string == "down":
      matrix[one] = 0
      one = (one[0], (one[1]+1)%jmax)
      matrix[one] = 1
      return movement
    else:
      return [[matrix[(i,j)]for i in range(imax)] for j in range(jmax)]
  return movement

