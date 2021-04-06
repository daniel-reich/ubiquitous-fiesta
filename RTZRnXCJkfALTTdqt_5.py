
def sum_neg(nums):
  return [] if len(nums) < 2 else [len(list(filter(lambda n: n > 0, nums))), sum(filter(lambda n: n < 0, nums))]

