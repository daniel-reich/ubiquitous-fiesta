
def sum_even_nums_in_range(start, stop):
  return sum(n for n in range(start, stop + 1) if not n % 2)

