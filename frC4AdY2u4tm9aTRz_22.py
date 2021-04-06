
def standard_deviation(lst):
  return round((sum(abs(sum(lst) / len(lst) - x) ** 2 for x in lst) / len(lst)) ** 0.5, 2)

