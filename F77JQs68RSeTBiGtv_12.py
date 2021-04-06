
def diamond_sum(n):
  i = int((n-1)/2)
  matrix = full_matrix(n)
  
  d_sum = 0
  
  for r in range(n):
    d_sum += matrix[r][i]
    if i != int((n-1)/2):
      d_sum += matrix[r][n-1-i]
    
    if r < int(n/2):
      i -= 1
    else:
      i += 1
      
  return d_sum
  
  
def full_matrix(n):
  matrix = []
  
  c_num = 1
  for r in range(n):
    vector = []
    for c in range(n):
      vector.append(c_num)
      c_num += 1
    matrix.append(vector)
  
  return matrix

