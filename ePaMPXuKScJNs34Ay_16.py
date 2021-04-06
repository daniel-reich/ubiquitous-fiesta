
def add_it_up(lst):
  return sum(lst) if type(lst[0]) in [int, float] else sum(lst, []) if type(lst[0]) == list else sum(lst, ())

