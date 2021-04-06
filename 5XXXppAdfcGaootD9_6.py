
def sum_odd_and_even(lst):
  even = 0
  odd = 0
  for i in lst:
    if i % 2 == 0:
      even += i
    else:
      odd += i
  return [even,odd]

