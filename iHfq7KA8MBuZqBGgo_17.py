
def is_legitimate(lst):
  return not any(lst[0] + lst[-1] + [x[0] + x[-1] for x in lst])

