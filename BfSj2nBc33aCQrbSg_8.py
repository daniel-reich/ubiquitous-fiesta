
def isprime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return n > 1
​
def truncatable(n):
  x = str(n)
  direction = {0:False, 1:"right", 2:"left", 3:"both"}
  d_in = 0
  if isprime(n) and "0" not in x:
    #right
    for i in range(1, len(x)):
      if isprime(int(x[:i])):
        continue
      else:
        break
    else:d_in += 1
    #left
    for i in range(1, (len(x))):
      if isprime(int(x[i:])):
        continue
      else:
        break
    else:d_in += 2
  
  return direction[d_in]

