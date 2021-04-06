
def kempner(n):
  i = 1
  k = 1
  while i < n:
    k *= i
    
    if k % n == 0:
      break
    i += 1
  return i

