
def sum_missing_numbers(lst):
  minimum = min(lst)
  maximum = max(lst)
  return sum(num for num in range(minimum, maximum + 1) if num not in lst)

