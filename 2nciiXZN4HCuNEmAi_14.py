
def flatten(r):
  lst = []
  for el in r:
    if isinstance(el,list):
      lst.extend(el)
    else:
      lst.append(el)
  if all(list(map(lambda x: isinstance(x,list) == False,lst))):
    return lst
  else:
    return flatten(lst)

