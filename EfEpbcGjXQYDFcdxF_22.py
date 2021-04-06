
def filter_list(l):
  li = []
  for x in l:
    if isinstance(x, int):
      li.append(x)
      
  return li

