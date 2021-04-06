
def multiply_nums(nums):
  x = 1
  for i in [int(i) for i in nums.split(", ")]:
    x *= i
  return x

