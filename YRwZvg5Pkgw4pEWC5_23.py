
def flick_switch(lst):
  new = []
  toggle = True
  for i in lst:
    if i=='flick':
      toggle = not toggle
    new.append(toggle)
  return new

