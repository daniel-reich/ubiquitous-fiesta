
def replace_next_largest(lst):
  sortedLst = sorted(lst)
  newLst = []
  lstMax = max(lst)
  for num in lst:
    if num == lstMax:
      newLst.append(-1)
    else:
      for numb in sortedLst:
        if numb > num:
          newLst.append(numb);
          break;
  return newLst

