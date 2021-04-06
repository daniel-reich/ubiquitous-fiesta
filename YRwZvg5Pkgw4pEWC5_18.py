
def flick_switch(lst):
  f = True
  o = []
  for i in lst:
    if i == 'flick':
      f = not f
    o.append(f)
  return o

