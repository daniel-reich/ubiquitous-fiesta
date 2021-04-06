
def ip(n):
  f = []
  for i in range(1, n):
    if n%i==0:f+=[i]
  return len(f)==1
def cuban_prime(num):
  a = []
  for y in range(100):
    a+=[3*y**2 + 3*y + 1]
  if num in a and ip(num): return str(num) + ' is cuban prime'
  else: return str(num) + ' is not cuban prime'

