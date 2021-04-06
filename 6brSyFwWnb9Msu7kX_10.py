
def pos_neg_sort(lst):
  plst = []
  for i in lst:
    if i >= 0:
      plst.append(i)
  a=0
  for j in range(len(lst)):
    if lst[j] >=0:
      lst[j] = sorted(plst)[a]
      a += 1
  return(lst)

