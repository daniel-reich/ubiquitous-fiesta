
from functools import reduce
def lcm_three(num):
  return reduce(lambda x,y:lcm(x,y),num)
​
def gcd(x,y):
    while y:
        x,y = y, x%y
    return x
​
def lcm(x,y):
    return x*y//gcd(x,y)

