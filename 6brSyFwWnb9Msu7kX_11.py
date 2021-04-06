
def pos_neg_sort(lst):
  l=[i for i in lst if i>0]
  l.sort()
  k=0
  for i,j in enumerate(lst):
    if j>0:
      lst[i]=l[k]
      k+=1
  return lst

