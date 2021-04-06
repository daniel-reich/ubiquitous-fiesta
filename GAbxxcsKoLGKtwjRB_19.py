
def isEven(n): 
  for i in range(2, n): 
    if n % i == 0: 
        return True
​
  return False
​
def sum_primes(lst): 
  if lst == []:
    return None
​
  total = 0
  for i in lst:
    if i == 1:
      continue
    if not isEven(i):
      total += i
​
  return total

