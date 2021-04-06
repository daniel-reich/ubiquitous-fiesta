
def get_only_evens(nums):
  lst = []
  for i in range(len(nums)):
    if i%2 == 0 and nums[i]%2 == 0:
      lst.append(nums[i])
  return lst

