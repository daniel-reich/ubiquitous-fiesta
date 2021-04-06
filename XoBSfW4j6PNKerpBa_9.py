
def complete_factorization(n):
  i = 2
  vals = []
  while n>1:
    while n%i:
      i+=1
    vals.append(i)
    n = n/i
    i = 2
​
​
  return vals

