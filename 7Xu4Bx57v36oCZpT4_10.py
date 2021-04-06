
def where_is_waldo(lst):
  r=0
  for l in lst:
    if len(set(l))==1:
      r+=1
      continue
    else:
      for e in set(l):
        if l.count(e)==1:
          return [r+1, l.index(e)+1]

