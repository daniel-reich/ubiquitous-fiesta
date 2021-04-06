
def sum_even_nums_in_range(start, stop):
  if start % 2 == 0:
    return sum([i for i in range(start,stop+1,2)])
  else:
    return sum([i for i in range(start+1,stop+1,2)])

