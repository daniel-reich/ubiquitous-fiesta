
def n_differences(lst):
  while len(lst) != 1:
    lst = [b - a for a, b in zip(lst, lst[1:])]
  return lst[0]

