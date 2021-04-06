
def sum_missing_numbers(lst):
  total = 0
  for number in range(min(lst), max(lst)+1):
    if number not in lst:
      total += number
  return total

