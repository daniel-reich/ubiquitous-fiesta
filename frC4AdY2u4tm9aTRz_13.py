
def standard_deviation(l):
  return round((sum((i-sum(l)/len(l))**2 for i in l)/len(l))**.5, 2)

