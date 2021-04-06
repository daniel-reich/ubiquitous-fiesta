
def standard_deviation(lst):
  mean = sum(lst) / len(lst)
  diffs = [abs(mean - i) for i in lst]
  return round((sum(i**2 for i in diffs) / len(lst)) ** 0.5, 2)

