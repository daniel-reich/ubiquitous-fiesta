
def sum_neg(nums):
  if nums == []:
    return []
  a = len([n for n in nums if n > 0])
  b = sum([n for n in nums if n < 0])
  return [a, b]

