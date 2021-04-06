
def almost_sorted(lst):
  if lst == sorted(lst) or lst == sorted(lst, reverse = True):
    return False
  for i in range(len(lst)):
    temp = lst.copy()
    temp.pop(i)
    if temp == sorted(temp) or temp == sorted(temp, reverse = True):
      return True
  return False

