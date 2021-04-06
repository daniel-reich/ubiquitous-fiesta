
def get_only_evens(nums):
  x = enumerate(nums)
  return [item[1] for item in x if item[0]%2 == 0 and item[1]%2 == 0 ]

