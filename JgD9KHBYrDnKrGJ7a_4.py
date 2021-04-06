
def swap_dict(dic):
  d = {}
  for i in dic:
    if dic[i] not in d:
      d[dic[i]] = [i]
    else:
      d[dic[i]].append(i)
  return d

