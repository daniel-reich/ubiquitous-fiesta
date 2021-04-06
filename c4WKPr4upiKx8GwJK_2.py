
def duplicate_nums(nums):
  A=[]
  B=[]
  for x in nums:
    if x not in A:
      A.append(x)
    else:
      B.append(x)
  if B:
    return sorted(B)
  else:
    return None

