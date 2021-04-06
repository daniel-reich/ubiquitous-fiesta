
def leader(lst):
  highest_number = max(lst)
  leader = lst.index(highest_number)
  lst2 = lst[leader:]
  result = []
  for i,v in enumerate(lst2):
    if i == 0 or i == (len(lst2) -1):
      result.append(v)
    elif i < (len(lst2) -1):
      if v > lst2[i+1]:
        result.append(v)
  return result

