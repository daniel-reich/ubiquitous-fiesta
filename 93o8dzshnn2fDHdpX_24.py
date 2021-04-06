
def lst_ele_sum(args):
  res = []
  for c in range(0,len(args)):
    res.append(sum([el for (i,el) in enumerate(args) if i != c]))
  return res

