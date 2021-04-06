
def rolls(lst):
  r=lst[0]
  for i in range(1,len(lst)):
    r+=lst[i]+(lst[i-1]==6)*lst[i]-(lst[i-1]==1)*lst[i]
  return r

