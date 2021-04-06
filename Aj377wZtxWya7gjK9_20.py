
def sum_missing_numbers(lst):
  f, t = min(lst), max(lst)
  return sum(x for x in range(f, t+1) if x not in lst)

