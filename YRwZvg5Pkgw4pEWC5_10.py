
def flick_switch(lst):
  cur = True
  arr = []
  for x in lst:
    if x == "flick":
      cur = not cur
    arr.append(cur)
  return arr

