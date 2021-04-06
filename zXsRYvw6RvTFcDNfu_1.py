
def ruth_aaron(n):
  f1, f2, f3 = fact(n), fact(n+1), fact(n-1)
  
  ruth = (f1[0] == f2[0]) + (f1[1] == f2[1])*2
  aaron = (f1[0] == f3[0]) + (f1[1] == f3[1])*2
  
  if ruth:
    return ['Ruth', ruth]
  if aaron:
    return ['Aaron', aaron]
  return False
  
def fact(n):
  factors = []
  for i in range(2, n+1):
    while not n%i:
      factors += [i]
      n //= i
  return (sum(set(factors)), sum(factors))

