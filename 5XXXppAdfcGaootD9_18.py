
def sum_odd_and_even(lst):
  return [sum(x for x in lst if not x%2), sum(x for x in lst if x%2)]

