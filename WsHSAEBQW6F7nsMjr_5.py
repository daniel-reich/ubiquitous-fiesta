
def flatten_the_curve(lst):
  if lst==[]:
    return []
  else:
    a=sum(lst)/len(lst)
    return [round(a,1)]*len(lst)

