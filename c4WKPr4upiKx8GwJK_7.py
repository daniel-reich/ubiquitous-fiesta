
def duplicate_nums(nums):
  lst = []
  lst2 = []
  
  for i in nums:
    if i not in lst:
      lst.append(i)
    else:
      lst2.append(i)
      
  return sorted(lst2) or None

