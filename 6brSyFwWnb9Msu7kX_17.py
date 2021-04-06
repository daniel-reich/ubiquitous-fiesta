
def pos_neg_sort(lst):
  l = sorted([i for i in lst if i > 0])
  for i in range(len(lst)):
    if lst[i] > 0:
      lst[i] = l.pop(0)
  return lst

