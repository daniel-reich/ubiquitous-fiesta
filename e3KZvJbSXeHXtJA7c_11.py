
def sum_missing_numbers(lst):
  low, high = min(lst), max(lst)
  return sum(list(range(low, 1 + high))) - sum(lst)

