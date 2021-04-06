
def sum_neg(lst):
  newlst = [0,0]
  if lst:
    for i in lst:
      if i < 0:
        newlst[1]+=i
      else:
        newlst[0]+=1
    return newlst
  else:
    return []

