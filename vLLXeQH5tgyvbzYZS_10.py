
def is_prim_pyth_triple(lst):
  m=min(lst)
  k=1
  for i in range(2,m):
    if lst[0]%i==0 and lst[1]%i==0 and lst[2]%i==0:
      k=k*i
  if k>1:
    return False
  else:
    k=max(lst)
    lst.remove(max(lst))
    if k**2==sum([k**2 for k in lst ]):
      return True
    else: 
      return False

