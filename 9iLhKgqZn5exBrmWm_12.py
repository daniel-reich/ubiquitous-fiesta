
def ascending(txt):
  factors = lambda x: [f for f in range(1,x) if not x%f]
  for i in factors(len(txt)):
    nums = [int(txt[s:s+i]) for s in range(0,len(txt),i)]
    print(sum(range(1,len(nums))))
    if sum(range(1,len(nums)))==(sum(nums) - (nums[0]*len(nums))):
      return True
    print(nums)
  return False

