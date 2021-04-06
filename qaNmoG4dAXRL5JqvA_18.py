
def sum_fractions(lst):
  count = 0
  for i in lst:
    count += (i[0] / i[1])
  return int(count)

