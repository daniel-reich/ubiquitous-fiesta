
def add_ending(lst, ending):
  for i in lst:
    lst[lst.index(i)] = i + ending
  return lst

