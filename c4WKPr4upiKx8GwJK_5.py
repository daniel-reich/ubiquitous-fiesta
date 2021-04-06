
def duplicate_nums(nums):
  res = list(set([i for i in nums if nums.count(i) == 2]))
  return None if res == [] else sorted(res)

