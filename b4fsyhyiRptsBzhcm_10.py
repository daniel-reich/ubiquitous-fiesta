
def sum_even_nums_in_range(start, stop):
  return sum(filter(lambda x: x % 2 == 0, range(start,stop+1)))

