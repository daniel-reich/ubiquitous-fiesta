
def multiply_nums(nums):
  ans = 1
  for i in nums.split(","):
    ans *= int(i)
  return ans

