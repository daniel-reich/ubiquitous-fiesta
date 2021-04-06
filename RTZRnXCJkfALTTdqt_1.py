
def sum_neg(lst):
  return lst and [sum(1 for x in lst if x>0), sum(x for x in lst if x<0)]

