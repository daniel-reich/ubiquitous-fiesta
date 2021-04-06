
def relation_lst(lst):
  lst = sorted(lst)
  ret = []
  for i in range(0,len(lst)):
    for j in range(i,len(lst)):
      ret.append((lst[i],lst[j]))
  return ret

