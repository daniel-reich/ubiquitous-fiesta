
def sum_of_cubes(nums):
  if len(nums) > 0:
    p = 0
    for elm in nums:
      p += elm**3
    return p
  return 0

