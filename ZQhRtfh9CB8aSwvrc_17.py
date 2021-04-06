
def greater_than_sum(nums):
  return all(nums[n] > sum(nums[m] for m in range(n)) for n in range(len(nums)))

