
def greater_than_sum(nums):
  return all(nums[x] > sum(nums[:x]) for x in range(1,len(nums)))

