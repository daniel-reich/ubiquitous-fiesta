
def moving_partition(lst):
  if len(lst) == 0:
    return []
  elif len(lst) == 1:
    return lst
  else:
    a = len(lst)
    result = []
    for i in range(a-1):
      temp = []
      temp.append(lst[:i+1])
      temp.append(lst[i+1:])
      result.append(temp)
    return result

