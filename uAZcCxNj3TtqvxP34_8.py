
def mode(nums):
  a = []
  for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
      a.append(nums[i])
  for i in range(1, len(a)):
    if a[i] != a[i-1]:
      pass
    else: 
      return mode(a)
  return a

