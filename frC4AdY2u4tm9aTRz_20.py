
def standard_deviation(lst):
  mn = sum(lst)/len(lst)
  l=[]
  for i in lst:
    sd=(i-mn)**2
    l.append(sd)
  return (round((sum(l)/len(lst))**0.5,2))

