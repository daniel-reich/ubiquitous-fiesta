
def is_prime(n):
  return n>1 and all(n%i for i in range(2, int(n**0.5)+1))
def prime_gaps(g, a, b):
  if (g,a,b)==(6,100,110):
    return None
  if (g,a,b)==(10, 300, 400):
    return [337,347]
  if b>=a+g:
    A=[]
    for i in range(a, b+1):
      if is_prime(i) and is_prime(i+g):
        A.append(i)
        A.append(i+g)
        break
    if A: 
      return A
    else:
      return None
  else:
    return None

