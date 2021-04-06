
def ones_infection(lst):
  cols = [list(i) for i in zip(*lst)]
  lst[:] = [[int(1 in lst[i] or 1 in cols[j]) for j in range(len(lst[0]))] for i in range(len(lst))]
  return lst

