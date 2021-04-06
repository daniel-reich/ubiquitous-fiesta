
def count_number(lst):
  return sum(count_number(i) if type(i) is list else type(i) in (int, float) for i in lst)

