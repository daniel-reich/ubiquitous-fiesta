
def duplicate_nums(nums):
  lst=[]
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i]==nums[j]:
        lst.append(nums[i])
  return None if len(lst)==0 else list(sorted(set(lst)))

