
def sum_odd_and_even(lst):
  sum_odd = 0
  sum_even = 0
  for i in lst:
    if i % 2:
      sum_odd += i
    else:
      sum_even += i
  return [sum_even, sum_odd]

