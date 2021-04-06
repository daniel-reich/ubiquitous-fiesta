
def move_to_end(lst, el):
  l = []
  g = []
  for x in lst:
    if x != el:
      l.append(x)
    else:
      g.append(x)
  return l+g

