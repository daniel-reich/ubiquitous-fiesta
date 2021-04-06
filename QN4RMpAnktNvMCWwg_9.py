
def id_mtrx(n):
  if isinstance(n, str):
    return "Error"
  
  matrix = []
  abs_n = abs(n)
  
  for idx in range(abs_n):
    inner_matrix = []
    for id in range(abs_n):
      if idx == id:
        inner_matrix.append(1)
      else:
        inner_matrix.append(0)
    if n > 0:
      matrix.append(inner_matrix)
    if n < 0:
      index = len(inner_matrix) - 1
      reverse_matrix = []
      while index >= 0:
        reverse_matrix.append(inner_matrix[index])
        index -= 1
      matrix.append(reverse_matrix)
      
  return matrix

