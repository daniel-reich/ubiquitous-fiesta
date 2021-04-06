
def make_dartboard(n):
  k = (1+n)//2
  quarter = ["".join(str(min(i+1,j+1)) for j in range(k)) for i in range(k)]
  half = [lev+lev[::-1][n%2:] for lev in quarter]
  full = half + half[::-1][n%2:]
  return [int(lev) for lev in full]

