
def greater_than_sum(nums):
  l=[sum(nums[:i]) for i in range(1,len(nums))]
  return all([x[1]-x[0]>0 for x in zip(l,nums[1:])])

