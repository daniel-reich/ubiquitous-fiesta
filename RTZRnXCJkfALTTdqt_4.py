
def sum_neg(nums):
  return [sum([1 for e in nums if e >= 0]), sum([e for e in nums if e < 0])] if nums else []

