
def less_or_equal(lst, k):
  lst.sort()
  for i in lst:
    if len([j for j in lst if j<=i])==k:
      return i
  if k==0 and min(lst)!=1:
    return 1

