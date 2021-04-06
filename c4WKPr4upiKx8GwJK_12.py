
def duplicate_nums(nums):
  res = sorted(list(set([el for el in nums if nums.count(el) > 1])))
  return None if len(res) == 0 else res

