
def duplicate_nums(nums):
  res = list(set([i for i in nums if nums.count(i) > 1])) 
  return sorted(res) if len(res) > 0 else None

