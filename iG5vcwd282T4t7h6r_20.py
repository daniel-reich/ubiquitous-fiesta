
def str_to_dict(lst):
  newlst = []
  keys = []
  values = []
  for i in lst:
    a = i.split("=")
    newlst.append(a)
  print(newlst)
  for i in range(len(newlst)):
    print(keys)
    keys.append(newlst[i][0])
    values.append(newlst[i][1])
  d = dict(zip(keys,values))
  return d

