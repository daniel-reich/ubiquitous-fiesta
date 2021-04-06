
def sum_of_evens(lst):
  return sum([sum([x for x in l if x % 2 == 0]) for l in lst])

