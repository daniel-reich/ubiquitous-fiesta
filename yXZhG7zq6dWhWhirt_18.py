
def prime(numb):
  import math
  if numb % 2 == 0 and numb >2 :
    return False
  elif numb == 1:
    return False
  for number in range(3,int(math.sqrt(numb))+1,2):
    if numb%number == 0:
      return False
  return True
​
def filter_primes(num):
  return list(filter(prime,num))

