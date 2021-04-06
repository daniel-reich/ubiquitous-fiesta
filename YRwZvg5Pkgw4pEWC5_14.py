
def flick_switch(lst):
  res = []
  item = True
  for el in lst:
    if el == "flick":
      item = not item
    res.append(item)
  return res

