
def diagonalize(n, d):
  l1= [[0 for x in range(n)] for x in range(n)]
  for i in range(0,n):
    for j in range(0,n):  
      if d == "ul": 
        l1[i][j] = i+j
      if d == "ur":
        l1[i][j] = n-1 + i - j
      if d == "lr":
        l1[i][j] = 2*(n-1) - i - j
      if d == "ll":
        l1[i][j] = n-1 + j - i
  return l1

