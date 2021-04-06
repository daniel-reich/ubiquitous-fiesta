
def bell(n):
  if n == 1: return 1
  triangle = [[i]*i for i in range(1,n+1)]
  triangle[1][0] = 1
  for i in range(2,n):
    for j in range(0,i+1):
      if j == 0:
        triangle[i][j] = triangle[i-1][-1]
      else:
        triangle[i][j] = triangle[i-1][j-1] + triangle[i][j-1]
  return triangle[n-1][-1]

