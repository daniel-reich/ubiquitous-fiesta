
def median(nums):
  if len(nums) % 2 != 0:
    return nums[(len(nums) // 2)]
  else:
    v = nums[(len(nums) // 2)] + nums[(len(nums) // 2) - 1]
    if v % 2 == 0:
      return v // 2
    else:
      return v // 2 + .5

