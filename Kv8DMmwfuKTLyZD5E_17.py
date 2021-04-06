
def make_dartboard(n):
  if n==1:return [1]
  w=[[0]*n for _ in range(n)]
  for k in range(1,int(n/2)+1):
   for i in range(n):
    for j in range(n):
     if i==n-k or j==n-k or i==k-1 or j==k-1:
         if w[i][j]==0:
                w[i][j]=k
  if n%2!=0: w[k][k]=k+1
  return [int("".join([str(j) for j in i])) for i in w]

