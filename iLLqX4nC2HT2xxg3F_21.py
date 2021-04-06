
def deepest(lst,d=1):
  if not any([isinstance(i,list) for i in lst]):
    return d
  else:
    return max([deepest(i,d+1) for i in lst if isinstance(i,list)])

