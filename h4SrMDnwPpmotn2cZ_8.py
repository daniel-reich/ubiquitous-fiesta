
def sum_of_cubes(nums):
  total_sum = 0
  for i in range(0, len(nums)):
    total_sum = total_sum + nums[i] ** 3
  return total_sum

