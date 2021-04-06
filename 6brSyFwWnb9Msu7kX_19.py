
def pos_neg_sort(lst):
  if lst==[]:
    return []
  ls=[]
  for i in lst:
    if i>0:
      ls.append(i)
      lst[lst.index(i)]=' '
  ls=sorted(ls)
  for i in ls:
    lst[lst.index(' ')]=i
  return lst

