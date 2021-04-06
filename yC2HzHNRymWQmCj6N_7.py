
def less_or_equal(lst, k):
  if k==0:
    for i in range(1,max(lst)):
      if len([j for j in lst if j<=i])==k:return i
  else:
    for i in range(min(lst),max(lst)+1):
      if len([j for j in lst if j<=i])==k:return i

