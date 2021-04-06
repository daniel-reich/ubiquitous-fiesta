
def sum_odd_and_even(lst):
  return [sum(n for n in lst if n % 2 == 0), sum(n for n in lst if n % 2)]

