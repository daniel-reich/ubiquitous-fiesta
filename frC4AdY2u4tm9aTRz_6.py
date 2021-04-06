
def standard_deviation(lst):
  m = sum(lst)/len(lst)
  return round((sum([abs(l-m)**2 for l in lst])/len(lst))**0.5,2)

