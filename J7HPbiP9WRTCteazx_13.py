
def n_differences(lst):
  return lst[0] if len(lst) == 1\
    else n_differences([b-a for a,b in zip(lst[:-1],lst[1:])])

