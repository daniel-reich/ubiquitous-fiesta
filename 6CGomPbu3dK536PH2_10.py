
def accumulating_list(lst):
  for i in range(1,len(lst)):lst[i]+=lst[i-1]
  return lst

