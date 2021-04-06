
def pos_neg_sort(lst):
  l = sorted([i for i in lst if i > 0])
  [l.insert(i, lst[i]) for i in range(len(lst)) if lst[i] < 0]
  return l

