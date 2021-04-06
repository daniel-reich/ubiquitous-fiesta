
def flick_switch(lst):
  change = True
  list = []
  for i in lst:
    if i == "flick":
      change = not change
    list.append(change)
  return list

