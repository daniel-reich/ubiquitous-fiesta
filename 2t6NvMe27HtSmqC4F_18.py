
def boolean_and(lst):
  if len(lst) == 2:
    return lst[0] and lst[1]
  else:
    return boolean_and([lst[0] and lst[1]] + lst[2:])
​
def boolean_or(lst):
  if len(lst) == 2:
    return lst[0] or lst[1]
  else:
    return boolean_or([lst[0] or lst[1]] + lst[2:])
​
def boolean_xor(lst):
  if len(lst) == 2:
    return lst[0] != lst[1]
  else:
    return boolean_xor([lst[0] != lst[1]] + lst[2:])

