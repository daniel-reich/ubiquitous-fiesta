
def flick_switch(lst):
  switch = True
  boolList = []
  for item in lst:
    if item != 'flick' and switch:
      boolList.append(switch)
    elif item == 'flick':
      switch = not switch
      boolList.append(switch)
    else:
      boolList.append(switch)
  return boolList

