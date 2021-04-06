
from functools import reduce
def multiply_nums(nums):
    return reduce(lambda x, y: x*y, [int(j) for j in nums.split(',')])

