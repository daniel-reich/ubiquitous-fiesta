
def count_missing_nums(lst):
  newlst = []
  for i in lst:
    try:
      newlst.append(int(i))
    except ValueError:
      continue
  finallst = []
  for i in range(min(newlst), max(newlst) + 1):
    finallst.append(i)
  return len(finallst) - len(newlst)

