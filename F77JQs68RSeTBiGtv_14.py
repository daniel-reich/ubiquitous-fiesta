
def diamond_sum(n):
  A=list(range(1, n**2+1))
  lst=[A[i:i+n] for i in range(0, len(A), n)]
  dsum=0
  for i in range(n):
    for j in range(n):
      if j+i==(n-1)//2 or j-i==-(n-1)//2 or j+i==3*(n-1)//2 or j-i==(n-1)//2:
        dsum+=lst[i][j]
  return dsum

