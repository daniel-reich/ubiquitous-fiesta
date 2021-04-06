
def even(a):
    return (a & 1)
def bitwise_index(lst):
  p={}
  for i in range(len(lst)):
    if even(lst[i])==0 and lst[i]>=0 and lst[i] not in p: p[lst[i]]=i
    else: pass
  if len(p)==0:
    d1="No even integer found!"
  elif even(p[max(p)])==0:
    x1='@even index '+str(p[max(p)])
    d1={x1:max(p)}
  else:
    x2='@odd index '+str(p[max(p)])
    d1={x2:max(p)}
  return d1

