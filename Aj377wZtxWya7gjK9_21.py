
def sum_missing_numbers(lst):
  lst.sort()
  whole = list(range(lst[0], lst[-1]+1))
  total = 0
  for num in whole:
    if not num in lst:
      total += num
  return total

