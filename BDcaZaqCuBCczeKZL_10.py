
def arrow(n):
  s = ['>' * x for x in range(1, n+1)]
  return s + [s, s[:-1]][n & 1][::-1]

