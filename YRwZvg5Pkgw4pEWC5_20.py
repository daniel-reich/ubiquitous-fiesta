
def flick_switch(lst):
  r = []
  s = True
  for x in lst:
    if x == "flick":
      s = not s
    r.append(s)
  return r

