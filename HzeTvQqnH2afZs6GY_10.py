
def generate_rug(n, direction):
  ans = list(row(n,j) for j in range(n))
  return ans if direction=='left' else ans[::-1]
def row(n,j):return list(i for i in range(1,j+1))[::-1] + [0] + list(i for i in range(1,n-j))

