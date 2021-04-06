
def sum_fractions(lst):
  y = []
  for i in lst:
    x = i[0] / i[1]
    y.append(x)
  return round(sum(y))

