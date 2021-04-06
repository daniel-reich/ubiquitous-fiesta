
def standard_deviation(lst):
  mean = sum(lst)/len(lst)
  differences = []
  for x in lst:
    differences.append((x-mean)**2)
  return round(((sum(differences)/len(lst))**.5), 2)

