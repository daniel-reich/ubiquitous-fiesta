
def count_number(lst):
  return sum(count_number(l) if type(l) == list else 0 if type(l) == str else 1 for l in lst)

