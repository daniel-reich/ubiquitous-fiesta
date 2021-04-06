
def make_sandwich(i, f):
  lst = []
  for el in i:
    if el == f:
      lst.extend(['bread', el, 'bread'])
    else:
      lst.append(el)
  return lst

