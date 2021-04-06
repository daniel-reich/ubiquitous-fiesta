
def sum_neg(lst):
  a = len([x for x in lst if x > 0])
  b = sum([x for x in lst if x < 0])
  if a ==0 and b == 0:
    return []
  return [a,b]

