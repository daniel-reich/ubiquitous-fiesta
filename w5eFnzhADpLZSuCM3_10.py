
def multiplicity(lst):
  a=[]
  for j in lst:
    if j not in a: a.append(j)
  ans=[]
  for i in a:
    ans.append([i,lst.count(i)])
  return ans

