
def is_ascending(s):
  for n in range(1,len(s)//2+1):
    nums = [s[i:i+n] for i in range(0, len(s), n)]
    if all([int(nums[i]) - int(nums[i-1]) == 1 for i in range(1,len(nums))]):
      return True
  return False

