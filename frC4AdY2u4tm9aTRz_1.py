
def standard_deviation(lst):
  m = sum(lst)/len(lst)
  s = 0 
  for i in lst:
    s = s + pow((i-m), 2)
  return round(pow((s/len(lst)), 0.5), 2)

