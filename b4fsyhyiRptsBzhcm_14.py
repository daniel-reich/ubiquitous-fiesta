
def sum_even_nums_in_range(start, stop):
  return sum([x for x in range(start, stop+1) if not x%2])

