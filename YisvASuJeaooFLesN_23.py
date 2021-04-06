
def max_total(nums):
  nums.sort()
  return nums[-5] + nums[-4] + nums[-3] + nums[-2] + nums[-1]

