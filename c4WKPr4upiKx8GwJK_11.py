
def duplicate_nums(nums):
  l = []
  d = []
  
  for i in nums:
    if i in l: d.append(i)
    else: l.append(i)
    
  return sorted(d) or None

