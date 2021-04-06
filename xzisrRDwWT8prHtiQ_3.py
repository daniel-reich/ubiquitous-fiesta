
def difference_two(lst):
  return [[i, i+2] for i in sorted(lst) if i+2 in lst]

