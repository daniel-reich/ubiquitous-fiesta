
def unique_lst(lst):
  return [n for (i,n) in enumerate(lst) if n > 0 and n not in lst[0:i]]

