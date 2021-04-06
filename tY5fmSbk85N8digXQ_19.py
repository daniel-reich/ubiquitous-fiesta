
def ones_infection(arr):
  #print(arr)
  c=len(arr[0])
  #print(c)
  r=len(arr)
  #print(r)
  res = [ [ 0 for i in range(c) ] for j in range(r) ]
  for row in range (r):
    for col in range(c):
      if arr[row][col]==1:
        for col_res in range (c):
          res[row][col_res]=1
        for row_res in range(r):
          res[row_res][col]=1
  for row in range (r):
    for col in range (c):
      arr[row][col]=res[row][col]
  return(arr)

