
def moving_partition(lst):
  ct = len(lst)
  part = 1
  if ct == 0:
    return []
  return helper(lst,[],ct,part)
  
def helper(lst,final,ct,part):  
  if ct == 1:
    return final
  else:
    final.append([lst[:part],lst[part:]])
    return helper(lst, final, ct - 1, part + 1)

