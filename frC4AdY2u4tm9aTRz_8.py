
def standard_deviation(lst):
  mean = sum(lst) / len(lst)
  ab_diff = [abs(i - mean) for i in lst]
  var = sum(i ** 2 for i in ab_diff) / len(lst)
  return round(var ** (1 / 2), 2)

