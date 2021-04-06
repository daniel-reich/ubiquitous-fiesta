
def boolean_and(lst):
  while len(lst) > 1:
    if lst[0] == True and lst[1] == True:
      lst[1] = True
    else:
      lst[1] = False
    lst.pop(0)
  return lst[0]
  
def boolean_or(lst):
  while len(lst) > 1:
    if lst[0] != lst[1] or lst[0] == True:
      lst[1] = True
    else:
      lst[1] = False
    lst.pop(0)
  return lst[0]
  
​
def boolean_xor(lst):
  while len(lst) > 1:
    if lst== [True,True]:
      return False
    else:
      if lst[0] == True and lst[1] == True:
        lst.pop(1)
      else:
        if lst[0] != lst[1]:
          lst[1] = True
        else:
          lst[1] = False
      lst.pop(0)
  
  return lst[0]

