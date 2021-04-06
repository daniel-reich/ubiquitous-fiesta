
def bridge_shuffle(lst1, lst2):
  ans=[]
  l1=len(lst1);l2=len(lst2)
  m=max(l1,l2)
  for i in range(m):
    if i<l1:ans.append(lst1[i])
    if i<l2:ans.append(lst2[i])
  return ans

