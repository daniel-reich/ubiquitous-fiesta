
def diagonalize(n, d):
  result = []
  
  if "u" in d:
    # ur
    if "r" in d:
      for row in range(n):
        result_row = []
        for col in range(n):
          result_row += [n-1-col+row]
        result += [result_row]
    
    # ul
    else:
      for row in range(n):
        result_row = []
        for col in range(n):
          result_row += [col+row]
        result += [result_row]
    
  else:
    max = (n-1)*2
    # lr
    if "r" in d:
      for row in range(n):
        result_row = []
        for col in range(n):
          result_row += [max-col-row]
        result += [result_row]
    
    # ll
    else:
      for row in range(n):
        result_row = []
        for col in range(n):
          result_row += [max-n+1+col-row]
        result += [result_row]
  
  return result

