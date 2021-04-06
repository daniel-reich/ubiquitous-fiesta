
def is_prim_pyth_triple(lst):
  i,t=2,0
  b=sorted(lst)
  while i<=b[0]:
    if b[0]%i==0 and b[1]%i==0 and b[2]%i==0:
      t=1
    i+=1
  if b[0]**2+b[1]**2==b[2]**2 and t==0:
    return True
  else:
    return False

