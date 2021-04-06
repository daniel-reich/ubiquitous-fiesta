
def swap_dict(dic):
  d = {}
  for i in dic:
    if dic[i] in d:
      d[dic[i]].append(i)
    else:
      d[dic[i]] = [i]
  return d

