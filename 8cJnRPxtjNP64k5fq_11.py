
def dance(lst, parameter):
  res = []
  if parameter == "men":
    for i in range(0,len(lst)):
      res.append([lst[i][0], lst[len(lst) - 1 - i][1]])
  else:
    for i in range(0,len(lst)):
      res.append([lst[len(lst) - 1 - i][0], lst[i][1]])
  return res

