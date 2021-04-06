
def is_positive_dominant(lst):
  a = [x for x in lst if x > 0]
  b = [y for y in lst if y < 0]
  return len(set(a)) > len(set(b))

