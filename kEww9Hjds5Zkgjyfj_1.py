
def replace_next_largest(lst):
  asc = sorted(lst) + [-1]
  return [asc[asc.index(i)+1] for i in lst]

