
def clear_ordering(lst):
  arr = {}
  for i in lst:
    if(arr.get(i[0])): return False
    else:
      arr.update({i[0]:i[1]})
      prr = [i for i in arr.values()]
      for j in prr:
        if prr.count(j) > 1: return False
  return True

