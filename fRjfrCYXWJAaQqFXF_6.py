
def check(n):
  if n == 1: 
    return False
  if n == 2:
    return True
  prime = True
  for i in range(2, n): 
    if n%i == 0:
      prime = False
  return prime
def primorial(n):
  l = []
  for i in range(1, 50): 
    if check(i): 
      l.append(i)
  count = 1
  for i in range(n): 
    count *= l[i]
  return count

