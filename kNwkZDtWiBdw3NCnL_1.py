
def can_nest(list1, list2):
  return all([min(list1)>min(list2),max(list1)<max(list2)])

