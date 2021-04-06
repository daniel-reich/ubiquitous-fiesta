
def can_nest(list1, list2):
  if max(list1) < max(list2) and min(list1) > min(list2): 
    return True
  else: 
    return False

