
def almost_uniform(nums):
  A=[]
  for i in range(len(nums)):
    B=[j for j in range(i+1, len(nums)) if nums[j]==nums[i] or nums[j]==nums[i]+1]
    T=[x for x in nums[i:B[-1]+1] if x==nums[i] or x==nums[i]+1] if B else []
    if T:
      A.append(T)
    C=[j for j in range(i+1, len(nums)) if nums[j]==nums[i] or nums[j]==nums[i]-1]
    S=[x for x in nums[i:C[-1]+1] if x==nums[i] or x==nums[i]-1] if C else []
    if S:
      A.append(S)
  res=[x for x in A if len(set(x))>1]
  return (len(max(res, key=len)) if res else 0) or quit()

