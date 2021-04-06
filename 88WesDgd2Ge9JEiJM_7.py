
def almost_uniform(nums):
  return max([nums.count(i)+nums.count(i+1) for i in nums if i+1 in nums]) if len(set(nums))>1 else 0

