
def sum_of_evens(lst):
  total = 0
  for l in lst:
    for e in l:
      if e % 2 == 0:
        total += e
  return total

