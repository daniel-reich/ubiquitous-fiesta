
def get_only_evens(nums):
  return [v for k,v in enumerate(nums) if k % 2 == 0 and v % 2 == 0]

