
def get_only_evens(nums):
  return [nums[i] for i in range(len(nums)) if i % 2 == 0 and nums[i] % 2 == 0]

