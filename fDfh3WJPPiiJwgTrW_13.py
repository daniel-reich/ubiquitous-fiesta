
def num_of_sublists(lst):
  for n in lst:
    if isinstance(n, list):
      return len(lst)
    else:
      return 0

