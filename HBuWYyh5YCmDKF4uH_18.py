
def almost_sorted(lst):
  t=[y-x>0 for x,y in zip(lst[:-1],lst[1:])]
  if t.count(True)>t.count(False):
    r=False
  else:
    r=True
  if lst==sorted(lst,reverse=r):
    return False
  for i in range(len(lst)-1):
    l=lst[:i]+lst[i+1:]
    if l==sorted(l,reverse=r):
      return True
  return lst[:-1]==sorted(lst[:-1],reverse=r)

