
def final_result(lst):
  if len(lst) == 1:
    return lst
  for i in range(1,len(lst)):
    if lst[i-1] == lst[i]:
      if i+2 <= len(lst) and lst[i-1] == lst[i+1]:
        return final_result(lst[:i-1]+lst[i+2:])
      return final_result(lst[:i-1]+lst[i+1:])
  return lst

