
def get_subsets(lst, target):
  results=[]
  for x in range(1, len(lst)+1):
    rr=[]
    subsets(lst,target,x,[],0,rr)
    if len(rr)>0:
      rr.sort()
      results=results+rr
  print(results)
  return results
def subsets(lst,target, n, ll, sm, result):
  if len(ll)==n:
    if sm==target:
      result.append(ll)
    return
  
  for i in range(0, len(lst)):
    ll2 = ll.copy()
    ll2.append(lst[i])
    sm2 = sm + lst[i]
    lst2 = lst[i+1:len(lst)]
    subsets(lst2, target, n, ll2, sm2, result)

