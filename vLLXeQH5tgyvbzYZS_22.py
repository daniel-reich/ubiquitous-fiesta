
def is_prim_pyth_triple(lst):
  sortlst = sorted(lst)
  if (pow(sortlst[0],2) + pow(sortlst[1],2)) == pow(sortlst[2],2) :
    for i in range(2, min(lst)+1):
      if (((lst[0]%i == 0) and (lst[1]%i == 0)) or ((lst[1]%i==0) and (lst[2]%i==0)) or ((lst[0]%i==0) and (lst[2]%i==0))):
        return False
    return True
  else:
    return False

