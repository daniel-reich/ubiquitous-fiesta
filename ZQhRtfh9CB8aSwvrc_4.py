
def greater_than_sum(nums):
  return all(nums[x + 1] > sum(nums[y] for y in range(x + 1)) for x in range(len(nums) - 1))

