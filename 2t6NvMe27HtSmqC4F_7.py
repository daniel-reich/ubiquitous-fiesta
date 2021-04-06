
def boolean_and(lst):
  if len(lst) > 2:
    a, b = lst.pop(0), lst.pop(0)
    lst.insert(0, a and b)
  else:
    return lst[0] and lst[1]
  return boolean_and(lst)
​
def boolean_or(lst):
  if len(lst) > 2:
    a, b = lst.pop(0), lst.pop(0)
    lst.insert(0, a or b)
  else:
    return lst[0] or lst[1]
  return boolean_or(lst)
​
def boolean_xor(lst):
  if len(lst) > 2:
    a, b = lst.pop(0), lst.pop(0)
    lst.insert(0, (a and not b) or (not a and b))
    print(lst[0])
  else:
    return (lst[0] and not lst[1]) or (not lst[0] and lst[1])
  return boolean_xor(lst)

