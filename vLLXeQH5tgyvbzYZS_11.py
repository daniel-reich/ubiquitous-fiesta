
def is_prim_pyth_triple(lst):
  lst.sort()
  count = 0
  for i in range(2,max(lst)):
    if(lst[0]%i == 0 and lst[1]%i == 0) and (lst[2]%i == 0):
      count = count + 1
  if((lst[0]**2 + lst[1]**2) == (lst[2]**2)) and (count==0):
    return True
  else:
    return False

