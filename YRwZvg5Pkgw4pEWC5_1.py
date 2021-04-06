
def flick_switch(lst):
  res = []
  flick = True
  for i in lst:
    if i == 'flick':
      flick = not flick
    res.append(flick)
  return res

