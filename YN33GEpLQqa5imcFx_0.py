
def pascals_triangle(n):
  f = lambda x: 1 if x == 0 else x * f(x-1)
  return ' '.join(str(int(f(n)/(f(k)*f(n-k)))) for k in range(n+1))

