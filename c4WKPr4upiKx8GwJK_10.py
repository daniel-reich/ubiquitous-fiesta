
def duplicate_nums(nums):
  l = list(set([i for i in nums if nums.count(i) > 1]))
  return None if len(l)<1 else sorted(l)

