
def swap_dict(dic):
  x = [i for i in dic]
  y = [dic[i] for i in dic]
  l = {}
  for i in range(len(x)):
    if y[i] not in l:
      l[y[i]] = [x[i]]
    else:
      l[y[i]] += [x[i]]
  return l

