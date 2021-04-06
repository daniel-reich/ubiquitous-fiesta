
def standard_deviation(nums):
  average = (sum(nums) / len(nums))
  newlist = []
  for item in nums:
      newlist.append(abs(item - average))
  added = 0
  for item in newlist:
      added = added + (item * item)
  step4 = added / len(nums)
  sqrt = step4**(1/2.0)
  value = round(sqrt, 2)
  return value

