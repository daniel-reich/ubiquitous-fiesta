
def sort_it(lst):
  return sorted(lst,key = lambda x: x if isinstance(x,int) else x[0])

