
def flatten_the_curve(lst):
  if lst==[]:
    return []
  return [round(sum(lst)/len(lst),1) for i in range(0,len(lst))]

