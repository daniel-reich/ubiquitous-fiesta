
def diagonalize(n, d):
  return [[i+j if d=='ul' else i-j+n-1 if d=='ur' else n+1-(i-j+2) if d=='ll' else n*2-i-j-2 for j in range(n)] for i in range(n)]

