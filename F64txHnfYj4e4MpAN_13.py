
def schoty(frame):
  nums = [len(f.split('---')[0]) for f in frame][::-1]
  
  res = 0
  for i in range(7):
    res += nums[i] * 10**i
  return res

