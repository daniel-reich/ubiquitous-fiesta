
def compress(lst):
  res = []
  mini = []
  l = len(lst)
  for i in range(l):
    if i != 0 and lst[i] != lst[i-1]:
      res.append(mini)
      mini = []
      mini.append(lst[i])
      if i == l - 1:
        res.append(mini)
    else:
      mini.append(lst[i])
      if i == l - 1:
        res.append(mini)
  result = [''.join(i) for i in res]
  return ''.join([i if len(i) == 1 else "{}{}".format(i[0], len(i)) for i in result])

