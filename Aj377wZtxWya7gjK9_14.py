
def sum_missing_numbers(lst):
  return sum(set(range(min(lst), max(lst))) - set(lst))

