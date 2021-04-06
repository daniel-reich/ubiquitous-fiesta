
def pos_neg_sort(lst):
  new = []
  a = 0
  cen = sorted(i for i in lst if i>0)
  for i in range(len(lst)):
    if lst[i]>0:
      new.append(cen[a])
      a+=1
    else:
      new.append(lst[i])
  return new

