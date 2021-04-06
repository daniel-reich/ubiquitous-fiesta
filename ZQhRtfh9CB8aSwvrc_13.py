
def greater_than_sum(nums):
  return all(sum(nums[:i])<nums[i] for i in range(len(nums)))

