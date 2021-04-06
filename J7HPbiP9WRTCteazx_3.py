
def n_differences(lst):
  while len(lst) > 1:
    newAry = []
    for i in range(0,len(lst) - 1):
      newAry.append(lst[i + 1] - lst[i])
    lst = newAry
  return(newAry[0])

