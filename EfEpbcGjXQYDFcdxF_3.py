
def filter_list(l):
  new = []
  for el in l:
    if type(el) == type(1):
      new.append(el)
  return new

