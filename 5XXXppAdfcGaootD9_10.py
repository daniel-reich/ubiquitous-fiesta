
def sum_odd_and_even(lst):
  evens = []
  odds = []
  for x in lst:
    if x % 2 == 0:
      evens.append(x)
    else : odds.append(x)
  return [sum(evens), sum(odds)]

