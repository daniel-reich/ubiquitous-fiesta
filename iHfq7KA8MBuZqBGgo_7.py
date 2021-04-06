
def is_legitimate(lst):
  return not any([x[0]  for x in lst]+[x[-1] for x in lst]+lst[0]+lst[-1])

