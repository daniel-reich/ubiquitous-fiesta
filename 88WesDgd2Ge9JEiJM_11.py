
def almost_uniform(nums):
  maxcount=0
  for i in set(nums):
    count=max(nums.count(i-1),nums.count(i+1))
    if count>0:maxcount=max(maxcount,count+nums.count(i))
  return maxcount

