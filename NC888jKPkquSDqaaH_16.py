
def clean_up(files, sort):
  k={'prefix':0,'suffix':1}[sort]
  lst = [e.split('.') for e in files]
  res=[[lst[0]]]
  for i in range(1,len(lst)):
    if lst[i][k]==lst[i-1][k]:res[-1]+=[lst[i]]
    else:res+=[[lst[i]]]
  return [[j for j in map('.'.join,i)] for i in res]

