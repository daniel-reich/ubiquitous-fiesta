
def sum_fractions(lst):
  total = 0
  for i in lst: 
    total += i[0] / i[1]
  return round(total, 0)

