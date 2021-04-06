
def sum_of_slices(lst):
  if len(lst) == 1:
    return lst
  res = []
  temp = 0
  skip = False
  for i in range(len(lst)-1):
    if temp == 0:
      temp += lst[i]
    if temp + lst[i+1] <= 100:
      temp += lst[i+1]
      skip = False
    else:
      res.append(temp)
      temp = 0
      skip = True
  if skip:
    res.append(lst[-1])
  return res

