
def generate_rug(n, d):
  return [[abs(i-j) for j in range(n)][::1 if d=='left' else -1] for i in range(n)]

