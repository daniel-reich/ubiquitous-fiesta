
def can_nest(list1, list2):
  if min(list1)>min(list2):
    if max(list1)<max(list2):
      return True
  return False

