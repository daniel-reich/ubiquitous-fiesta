
def to_list(dct):
  lst = []
  for tpl in dct.items():
    lst.append(list(tpl))
  lst.sort()
  return lst

