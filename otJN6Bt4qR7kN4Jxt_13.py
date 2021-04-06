
def incremental_depth(lst):
  if len(lst) > 1:
    return [lst[0], incremental_depth(lst[1:])]
  return [lst[0]]

