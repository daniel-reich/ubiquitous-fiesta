
def multiplicity(lst):
  nums = []
  ret = []
  for i in lst:
    if i not in nums:
      nums.append(i)
  for i in nums:
    tmp = [i,lst.count(i)]
    ret.append(tmp)
  return ret

