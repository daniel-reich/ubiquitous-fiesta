
standard_deviation = lambda r: \
  round((sum((x-sum(r)/len(r))**2 for x in r)/len(r))**0.5, 2)

