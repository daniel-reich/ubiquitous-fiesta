
def incremental_depth(lst):
  if len(lst) == 1:
    return lst
  if len(lst) == 2:
    return [lst[0],[lst[1]]]
  return [lst[0],[lst[1], incremental_depth(lst[2:])]]

