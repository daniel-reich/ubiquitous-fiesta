
def flatten_the_curve(lst):
  if len(lst)==0:
    return lst
  avg=round(sum(lst)/len(lst),1)
  for i in range(len(lst)):
    lst[i]=avg
  return lst

