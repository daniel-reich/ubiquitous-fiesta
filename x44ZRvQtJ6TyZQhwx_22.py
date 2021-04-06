
def is_pandigital(n):
  n = set([int(num) for num in str(n)])
  
  for i in range(10):
    if not i in n:
      return False
​
  return True

