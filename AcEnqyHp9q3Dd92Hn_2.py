
def multiply_nums(nums):
  x = 1
  for i in nums.split(","):
    x *= int(i)
  return x

