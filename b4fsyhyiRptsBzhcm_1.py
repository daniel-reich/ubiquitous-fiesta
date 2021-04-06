
def sum_even_nums_in_range(start, stop):
  return sum([i for i in range(start+start%2, stop+1, 2)])

