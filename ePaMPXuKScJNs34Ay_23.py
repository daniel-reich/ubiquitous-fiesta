
def add_it_up(lst):
  try:
    return sum(lst)
  except:
    x = [z for i in lst for z in i]
    return tuple(x) if isinstance(lst[0], tuple) else x

