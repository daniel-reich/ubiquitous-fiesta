
def sum_even_nums_in_range(start, stop):
  a= list(filter(lambda x: x%2==0, range(start,stop+1)))
  return sum(a)

