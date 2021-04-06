
def matrix(n):
  m = [[j for j in range(1,n+1)],[3*n - 2 - j for j in range(0,n)]]
  if n == 2:
    return m
  else:
    for i in range(1,n-1):
      m.insert(i,([0 for j in range(0,n-2)]))
      m[i].insert(0,4*(n-1)-i+1)
      m[i].append(n+i)
  
  m[0][0] = 1
  r,c = 1,0
  while m[r][c] < n * n:
    while m[r][c+1] == 0:
      c += 1
      m[r][c] = m[r][c-1] + 1 
    while m[r+1][c] == 0:
      r += 1
      m[r][c] = m[r-1][c] + 1 
    while m[r][c-1] == 0:
      c -= 1
      m[r][c] = m[r][c+1] + 1 
    while m[r-1][c] == 0:
      r -= 1
      m[r][c] = m[r+1][c] + 1 
  return m

