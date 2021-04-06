
def sum_missing_numbers(lst):
  return sum(range(min(lst), max(lst) + 1)) - sum(lst)

