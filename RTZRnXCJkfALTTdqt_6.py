
def sum_neg(nums):
  if(not nums): return []
  pos = [] 
  neg = []
  for x in nums : neg.append(x) if x < 0 else pos.append(x)
  return  [len(pos), sum(neg)]

