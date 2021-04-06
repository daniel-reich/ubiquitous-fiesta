
def sort_it(lst):
  lst.sort(key = lambda x: x[0] if isinstance(x,list) else x)
  return lst

