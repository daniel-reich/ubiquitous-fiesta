
from math import factorial as fact
​
def eval_factorial(lst):
  nums = map(lambda s: int(s[:-1]),
             lst)
  return sum(map(fact, nums))

