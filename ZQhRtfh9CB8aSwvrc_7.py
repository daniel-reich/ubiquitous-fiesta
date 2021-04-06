
def greater_than_sum(nums):
  return all(nums[i] > sum(nums[:i]) for i in range(1, len(nums)))

