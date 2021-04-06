
def bell(n):
  x = [[0 for i in range(n+1)] for j in range(n+1)]
  print(x)
  x[0][0] = 1
  print(x)
  for i in range(1, n+1):
    x[i][0] = x[i-1][i-1]
    for j in range(1,i+1):
      x[i][j] = x[i-1][j-1] + x[i][j-1]
    print(x)
  return x[n][0]

