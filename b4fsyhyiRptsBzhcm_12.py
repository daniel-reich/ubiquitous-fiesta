
def sum_even_nums_in_range(start, stop):
  return sum(list(filter(lambda e : e % 2 == 0 , range(start , stop+1))));

