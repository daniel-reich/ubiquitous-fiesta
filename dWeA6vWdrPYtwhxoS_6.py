
def count_number(lst):
  if type(lst) == list:
    return sum(map(count_number, lst))
  return 1 if type(lst) == int or type(lst) == float else 0

