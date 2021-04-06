
def sum_missing_numbers(lst):
  lst.sort()
  return sum(i for i in range(lst[0], lst[-1]) if i not in lst)

