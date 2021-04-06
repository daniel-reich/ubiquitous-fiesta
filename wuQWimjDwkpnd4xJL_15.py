
def balanced(lst):
  a = int(len(lst) / 2)
  aa = lst[ : a]
  bb = lst[a : ]
  if  sum(aa) == sum(bb):
    return lst
  elif sum(bb) > sum(aa) :
    return bb + bb
  else:
    return aa + aa

