
def accumulating_list(lst):
  if lst == []:
    return []
  newlst = [lst[0]]
  num = lst[0]
  for i in range(len(lst)-1):
    num = num + lst[i+1]
    newlst.append(num)
  return newlst

