
def duplicate_nums(nums):
  
  already_used = []
  duplicates = set()
  
  for num in nums:
    if num not in already_used:
      already_used.append(num)
    else:
      duplicates.add(num)
  
  if len(list(duplicates)) == 0:
    return None
  return sorted(list(duplicates))

