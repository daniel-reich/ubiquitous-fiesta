
def sum_list(lst):
  return sum(sum_list(n) if type(n) == list else n for n in lst)

