
def multiply_nums(nums):
  n = nums.split(",")
  nn = [x.strip() for x in n]
  nnn = [int(y) for y in nn]
  prod = 1
  for i in nnn:
    prod *= i
  return prod

