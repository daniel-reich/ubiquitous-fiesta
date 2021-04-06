
def sum_odd_and_even(lst):
  even_sum, odd_sum = 0, 0
  for n in lst:
    if not n%2:
      even_sum += n
    else:
      odd_sum += n
  return [even_sum, odd_sum]

