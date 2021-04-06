
def generateRug(n, direction):
  return [[abs(i-j) for i in range(n)] for j in range(n)] if direction=='left' else [[abs(i-j) for i in range(n-1,-1,-1)] for j in range(n)]

