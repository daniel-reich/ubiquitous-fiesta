
def sum_neg(nums):
  if not nums or len(nums) is 0:
    return []
  p = [x for x in nums if x > 0]
  n = [x for x in nums if x < 0]
  return [len(p), sum(n)]

