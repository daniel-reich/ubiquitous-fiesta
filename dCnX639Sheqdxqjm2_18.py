
def parallel_resistance(lst):
  reverse_total = 0
  for num in lst:
    reverse_total += (1/num)
  return round(reverse_total**(-1), 1)

