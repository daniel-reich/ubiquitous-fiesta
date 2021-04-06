
def flick_switch(lst):
  a = True
  r = []
  for i in lst:
    if i=='flick':
      a = not a
    r.append(a)
  return r

