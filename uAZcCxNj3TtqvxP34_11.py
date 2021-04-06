
def mode(nums):    
  maxkey=max(set(nums), key = nums.count)
  maxValue=nums.count(maxkey)
  return sorted(list(set(i for i in nums if nums.count(i)==maxValue)))

