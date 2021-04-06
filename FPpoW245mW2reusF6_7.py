
def even_last(lst):
  return sum(lst[::2])*lst[-1] if len(lst)>0 else 0

