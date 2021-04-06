
def count_number(lst):
  if type(lst)!=list: return 1 if type(lst) in [int,float] else 0
  return sum(count_number(a) for a in lst)

