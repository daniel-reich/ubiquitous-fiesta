
def simple_equation(a, b, c):
  nums = [a,b,c]
  for i in range(3):
    if nums[0]+nums[1]==nums[2]:
      return '{0}+{1}={2}'.format(nums[0],nums[1],nums[2])
    if nums[0]-nums[1]==nums[2]:
      return '{0}-{1}={2}'.format(nums[0],nums[1],nums[2])
    if nums[0]*nums[1]==nums[2]:
      return '{0}*{1}={2}'.format(nums[0],nums[1],nums[2])
    if nums[0]/nums[1]==nums[2]:
      return '{0}/{1}={2}'.format(nums[0],nums[1],nums[2])
    nums = nums[1:]+[nums[0]]
  return ''

