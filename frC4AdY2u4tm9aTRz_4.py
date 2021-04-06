
def standard_deviation(lst):
  avg = sum(lst) / len(lst)
  return round((sum([(ele - avg)**2 for ele in lst]) / len(lst)) ** .5, 2)

