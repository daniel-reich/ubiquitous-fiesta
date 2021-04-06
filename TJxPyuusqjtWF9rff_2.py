
def get_only_evens(nums):
  return [n for idx, n in enumerate(nums) if not idx%2 and not n%2]

