
def get_only_evens(nums):
  even = []
  for i in range(len(nums)):
    if i%2==0 and nums[i]%2 ==0:
      even.append(nums[i])
  return even

