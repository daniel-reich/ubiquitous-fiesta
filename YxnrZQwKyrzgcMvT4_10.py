
def rotate_transform(lst, num):
  matrix = {(i,j): char for j, line in enumerate(lst) for i,char in enumerate(line)}
  imax = max([coord[0] for coord in matrix.keys()])
  jmax = max([coord[1] for coord in matrix.keys()])
  if num > 0:
    for _ in range(num):
      matrix = {(i,j): matrix[j,imax-i] for j, line in enumerate(lst) for i,char in enumerate(line)}
  else:
    for _ in range(abs(num)):
      matrix = {(i,j): matrix[jmax-j,i] for j, line in enumerate(lst) for i,char in enumerate(line)}
  
  lines = []
  for j in range(jmax+1):
    line = []
    for i in range(imax+1):
      line.append(matrix[(i,j)])
    lines.append(line)
  return lines

