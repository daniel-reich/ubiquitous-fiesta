
def greater_than_sum(nums):
  return all(y > sum(nums[0:x]) for x,y in enumerate(nums));

