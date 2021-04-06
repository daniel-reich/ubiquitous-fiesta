
def sum_odd_and_even(lst):
  return [sum(n * (n % 2 == i) for n in lst) for i in (0, 1)]

