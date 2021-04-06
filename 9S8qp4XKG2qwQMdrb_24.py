
from math import factorial
def ways_to_climb(n1,n2=0,total=0):
  total += factorial(n1+n2)//(factorial(n1)*factorial(n2))
​
  if n1 < 2:
    return total
  else:
    n1, n2 = n1-2, n2+1
    return ways_to_climb(n1,n2,total)

