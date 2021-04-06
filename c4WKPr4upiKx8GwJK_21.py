
def duplicate_nums(nums):
  myans = []
  for i in range(len(nums)):
    if nums[i] in nums[i+1:] and nums[i] not in myans:
      myans.append(nums[i])
  if len(myans) == 0:
    return None
  return sorted(myans)

