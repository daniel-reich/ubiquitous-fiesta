
def multiplication_table(n):
  if n == 1:
    return [[1]]
    
  temp = [x for x in range(1, n+1)]
  arr_res = [temp]
  for _ in range(n-1):
    temp = [x+j+1 for j, x in enumerate(temp)]
    arr_res.append(temp)
  return arr_res

