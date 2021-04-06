
def diamond_sum(n):
  # i tried
  
  n = (n+1) / 2
  centre = 2*n**2 - 2*n + 1
  return 1 if n == 1 else centre * 4 * (n-1)

