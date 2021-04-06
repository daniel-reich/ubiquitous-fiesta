
def id_mtrx(n):
  
  if type(n) != int:  
    return "Error"
​
  if n == 0:
    return [0]
​
  if n > 0:
    matrix = []
    for row in range(n):
      row =[]
      for i in range(n):
        row.append(0)
      matrix.append(row)
  
    for i in range(n):
      matrix[i][i] = 1
    
    return matrix
    
  if n < 0:
    n = n * (-1)
    matrix = []
    for row in range(n):
      row =[]
      for i in range(n):
        row.append(0)
      matrix.append(row)
    
    i = 0
    j = -1
    while i < n:
      matrix[i][j] = 1
      i += 1
      j -= 1
    return matrix

