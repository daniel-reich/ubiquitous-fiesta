
def can_nest(list1, list2):
  return True if min(list1) > min(list2) else False if max(list1) < max(list2) else False

