
def sum_of_evens(lst):
  total = 0
  for el in lst:
    total += sum([num for num in el if num % 2 == 0])
  return total

