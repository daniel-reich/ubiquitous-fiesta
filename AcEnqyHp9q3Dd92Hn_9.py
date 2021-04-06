
from numpy import prod
def multiply_nums(nums):
  return prod([int(i) for i in nums.split(', ')])

