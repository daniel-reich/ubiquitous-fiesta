
from math import factorial
​
def mod(base, key):
  loop = 1
  last_item = 1
  for i in range(1, min(base, key)):
    loop += last_item*i
    last_item *= i
  return loop % factorial(key)

