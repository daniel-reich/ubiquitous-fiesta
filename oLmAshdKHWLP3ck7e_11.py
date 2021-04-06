
def min_difference_pair(nums):
  nums.sort()
  minimo=abs(nums[0]-nums[1])
  lista=[nums[0],nums[1]]
  for x in range (len(nums)-1):
    if abs(nums[x]-nums[x+1])<minimo:
      minimo=abs(nums[x]-nums[x+1])
      lista=[nums[x],nums[x+1]]
    elif abs(nums[x]-nums[x+1])==minimo:
      lista=lista+[nums[x],nums[x+1]]
  return lista[:2]

