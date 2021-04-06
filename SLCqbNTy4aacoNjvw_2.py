
def remove_dups(lst):
  return [x for n,x in enumerate(lst) if x not in lst[:n]]

