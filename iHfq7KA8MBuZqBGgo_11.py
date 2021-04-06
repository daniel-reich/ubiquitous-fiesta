
def is_legitimate(lst):
  return 1 not in lst[0] + [x for y in [[x[0], x[-1]] for x in lst[1:-1]] for x in y] + lst[-1]

