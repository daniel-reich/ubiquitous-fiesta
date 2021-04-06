
def moving_partition(lst):
  if(lst == []):
    return lst
  elif(len(lst) == 1):
    return []
  else:
    res = []
    for i in range(1,(len(lst))):
      r1 = lst[0:i]
      r2 = lst[i:]
      k = [r1,r2]
      res.append(k)
    return res

