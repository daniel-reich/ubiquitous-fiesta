
def arrow(n):
  return ['>' * i for i in range(1, n+1)] + ['>' * i for i in range(n-n%2, 0, -1)]

