
def moving_partition(lst):
  if lst:
    ans=[]
    for i in range(1,len(lst)):
      a=[]
      a.append(lst[:i])
      a.append(lst[i:])
      ans.append(a)
    return ans
  return []

