
def final(r, c, i):
  row = [0 for x in range(c)]
  matrix = [row.copy() for x in range(r)]
​
  for inst in i:
    if inst[-1] == "r":
      matrix[int(inst[0])] = [i+1 for i in matrix[int(inst[0])]]
    else:
      for j in range(r):
        matrix[j][int(inst[0])]  = matrix[j][int(inst[0])] + 1
      
  return matrix

