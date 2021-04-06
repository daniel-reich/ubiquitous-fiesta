
def n_differences(lst):
  if len(lst) == 1:
    return lst[0]
  else:
    return n_differences([b-a for a, b in zip(lst, lst[1:])])

