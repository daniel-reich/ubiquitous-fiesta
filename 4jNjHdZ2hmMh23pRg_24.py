
def cutting_grass(lst, *cuts):
  res = []
  for i in cuts:
    lst = [lst[k]-i for k in range(len(lst))]
    if len([x for x in lst if x<=0])==0:
      res+=[lst]
    else:
      res+=['Done']
  return res

