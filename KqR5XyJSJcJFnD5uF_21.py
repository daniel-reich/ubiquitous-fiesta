
def median(nums):
  s = sorted(nums)
  if len(nums)%2==0: return (s[len(nums)//2] + s[len(nums)//2-1] )/2
  else: return s[len(nums)//2]

