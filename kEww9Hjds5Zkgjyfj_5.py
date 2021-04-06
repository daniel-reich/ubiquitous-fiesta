
def replace_next_largest(lst):
  x = sorted(lst)+[-1]
  return [x[x.index(i)+1] for i in lst]

