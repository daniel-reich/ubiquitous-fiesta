
def landscape_type(lst):
  while lst[0]==lst[1]:lst=lst[1:]
  while lst[-1]==lst[-2]:lst=lst[:-1]
  l=[i[1]-i[0] for i in zip(lst,lst[1:])]
  if 0 in l: return "neither"
  l=[i>0 for i in l]
  if all(l) or not any(l): return 'neither'
  for i in range(1,len(l)-1):
    if l[i-1]==l[i+1]!=l[i]: return "neither"
  return "mountain" if l[0] else "valley"

