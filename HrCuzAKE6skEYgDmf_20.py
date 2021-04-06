
def pairs(lst):
  newlst = []
  length = 0
  if len(lst) % 2 == 0:
    length = len(lst) // 2
  else:
    length = (len(lst) // 2) + 1
  for i in range(length):
    newlst.append([lst[i], lst[len(lst) - i - 1]])
  return newlst

