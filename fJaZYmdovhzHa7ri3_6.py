
def max_collatz(n, mx=1):
  return mx if n==1 else max_collatz([n//2, n*3+1][n%2], \
    max(n,mx, [n//2, n*3+1][n%2]))

