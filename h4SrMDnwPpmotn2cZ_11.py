
def sum_of_cubes(nums):
  if len(nums) == 0:
    return 0
  else:
    c = [c ** 3 for c in nums]
    return sum(c)

