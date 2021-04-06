
def landscape_type(lst):
  status = "unknown"
  peak = max(lst)
  trough = min(lst)
  index1 = lst.index(peak)
  index2 = lst.index(trough)
  if lst.count(peak) == 1 and index1 > 0 and index1 < len(lst) - 1:
    lst1 = lst[:index1]
    lst2 = lst[index1::]
    ascend = sorted(lst1)
    descend = sorted(lst2,reverse = True)
    if lst1 == ascend and lst2 == descend:
      status = "mountain"
  if status == "unknown":
    if lst.count(trough) == 1 and index2 > 0 and index2 < len(lst) - 1:
      lst3 = lst[:index2]
      lst4 = lst[index2::]
      ascend2 = sorted(lst4)
      descend2 = sorted(lst3, reverse = True)
      if lst3 == descend2 and lst4 == ascend2:
        status = "valley"
  if status == "unknown":
    status = "neither"
      
    
  return status

