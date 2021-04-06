
from random import *
​
def numbers():
  nums = list(range(1, 6))
  shuffle(nums)
  return int(''.join(map(str, nums)))

