
def sum_of_evens(lst):
  return sum(n for l in lst for n in l if n % 2 == 0)

