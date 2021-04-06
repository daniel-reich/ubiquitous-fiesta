
def pos_neg_sort(lst):
  pos = sorted([i for i in lst if i > 0])
  it = 0
  for i in range(len(lst)):
    if lst[i] > 0:
      lst[i] = pos[it]
      it += 1
  return lst

