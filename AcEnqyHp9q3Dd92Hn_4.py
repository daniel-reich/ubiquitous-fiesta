
import numpy
def multiply_nums(nums):
  return numpy.prod([int(i) for i in nums.split(', ')])

