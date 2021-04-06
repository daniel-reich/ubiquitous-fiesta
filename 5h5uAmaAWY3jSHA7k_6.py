
def landscape_type(lst):
  if mountain(lst):
    return 'mountain'
  elif valley(lst):
    return 'valley'
  return 'neither'
  
def mountain(lst):
  m = max(lst)
  i = lst.index(m)
  if i != 0 and i != len(lst)-1 and lst[:i+1] == sorted(lst[:i+1]) and lst[i:] == sorted(lst[i:], reverse = True):
    return 1
  return 0
  
def valley(lst):
  m = min(lst)
  i = lst.index(m)
  if i != 0 and i != len(lst)-1 and lst[:i+1] == sorted(lst[:i+1], reverse = True) and lst[i:] == sorted(lst[i:]):
    return 1
  return 0

