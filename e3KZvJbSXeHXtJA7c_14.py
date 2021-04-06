
def sum_missing_numbers(lst):
  return sum(n for n in range(sorted(lst)[0], sorted(lst)[-1]) if n not in lst)

