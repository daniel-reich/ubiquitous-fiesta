
def numbers_to_ranges(lst):
  res = []; temp = []
  for i in range(len(lst)):
    if not temp:
      temp.append(lst[i])
    elif lst[i] == temp[-1] + 1:
      temp.append(lst[i])
    else:
      res.append(temp)
      temp = [lst[i]]
  if temp:
    res.append(temp)
  return ['{}-{}'.format(i[0],i[-1]) if len(i) > 1 else str(i[0]) for i in res]

