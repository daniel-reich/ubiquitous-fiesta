
def accumulating_list(lst):
  if len(lst) == 0:
    return []
  else:
    temp = []
    mysum = 0
    for item in lst:
      mysum += item
      temp.append(mysum)
  return temp

