
def sum_odd_and_even(lst):
  x = lst[::2]
  y = lst[1::2]
  return [sum(y), sum(x)]

