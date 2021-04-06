
def standard_deviation(lst):
  m = sum(lst)/len(lst)
  return round(((sum([abs(i - m)**2 for i in lst]))/len(lst))**0.5,2)

