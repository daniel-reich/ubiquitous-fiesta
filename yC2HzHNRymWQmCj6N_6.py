
def less_or_equal(lst, k):
  if k==0 and (len(lst)>1 or lst[0]!=1):
    return 1
  for i in lst:
    cur = 0
    for j in lst:
      if j<=i:
        cur+=1
    if cur==k:
      return i

