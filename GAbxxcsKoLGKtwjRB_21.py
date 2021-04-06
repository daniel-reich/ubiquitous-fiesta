
def sum_primes(lst):
  s = 0
  n = 0
  if len(lst) == 0:
    return None
  else:
    for i in lst:
      for j in range(2,i+1):
        if i%j == 0 and j != i :
          n = 0
          break
        else:
          n = i
​
      if n != 0:
        s += n
        n = 0
  return s

