
from functools import reduce
​
def max_product(n):
  highest = 1
  ret = []
  for i in range(n+1):
    prod = reduce((lambda x, y: x * y), [int(digit) for digit in str(i)])
    if prod > highest:
      highest = prod
      ret = [i]
    elif prod == highest:
      ret.append(i)
    
  return ret

