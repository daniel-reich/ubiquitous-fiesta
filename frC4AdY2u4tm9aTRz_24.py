
def standard_deviation(lst):
  mean=sum(lst)/len(lst)
  s=[]
  for i in lst:
    s.append((i-mean)**2)
  d= sum(s)/len(lst)
  return round(d**(1/2),2)

