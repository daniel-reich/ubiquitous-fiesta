
def sort_it(lst):
  z = list(zip([x[0] if type(x) == list else x for x in lst], lst))
  print(z)
  r = sorted(z)
  return [x[1] for x in r]

