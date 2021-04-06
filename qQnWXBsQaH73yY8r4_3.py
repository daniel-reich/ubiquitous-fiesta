
def kempner(n):
  mult = 1
  for x in range(1 , n+1):
    mult *= x
    if mult % n == 0:
      return (x)

