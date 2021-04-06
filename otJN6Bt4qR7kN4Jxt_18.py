
def incremental_depth(lst,i=0):
  if i == len(lst)-1:
    return [lst[i]]
  return [lst[i]] + [incremental_depth(lst,i+1)]

