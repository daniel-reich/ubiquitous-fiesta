
def sum_neg(lst):
  if not lst:
    return []
  else:
    return [len([x for x in lst if x > 0])] + [sum(y for y in lst if y < 0)]

