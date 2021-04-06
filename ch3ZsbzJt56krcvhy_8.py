
def square_root(n):
  k = len(str(n))
  x = 10**(k//2)
  for i in range(15):
    x = (x + n//x)//2
  if x**2 == n: return x
  if (x-1)**2 == n: return x-1
  if (x+1)**2 == n: return x+1

