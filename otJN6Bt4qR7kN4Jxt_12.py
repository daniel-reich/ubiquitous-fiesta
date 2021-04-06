
def incremental_depth(lst):
  return lst if len(lst)==1 else [lst[0], incremental_depth(lst[1:])]

