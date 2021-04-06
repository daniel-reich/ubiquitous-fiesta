
def multiply_nums(nums):
  p = 1
  for x in map(int, nums.split(', ')):
    p *= x
  return p

