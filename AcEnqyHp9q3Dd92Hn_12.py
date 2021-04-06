
def multiply_nums(nums):
  list = nums.split(", ")
  result = 1
  for n in list:
    result*=int(n)
  return result

