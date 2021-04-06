
def sum_odd_and_even(lst):
  return [sum(e for e in lst if e%2==i) for i in [0,1]]

