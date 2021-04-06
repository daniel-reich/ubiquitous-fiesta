
def mode(nums):
  modeFreq = max([nums.count(i) for i in nums])
  res = []
  for i in nums:
    if nums.count(i)==modeFreq and not i in res:
      res.append(i)
  return res

