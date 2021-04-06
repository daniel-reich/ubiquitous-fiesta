
def sum_missing_numbers(lst):
  return sum([x for x in range(min(lst), max(lst)+1) if x not in lst])

