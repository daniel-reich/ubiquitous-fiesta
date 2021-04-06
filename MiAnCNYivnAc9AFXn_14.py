
def change_types(l):
  m = []
  for x in l:
    if isinstance(x, str): 
      x = x.title() + "!"
      m.append(x)
    elif isinstance(x, bool): 
      x = not x
      m.append(x)
    elif x % 2 == 0: 
      x += 1
      m.append(x)
    else: 
      x = x
      m.append(x)
  return m

