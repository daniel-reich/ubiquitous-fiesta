
def sum_neg(lst):
  return [sum(1 for x in lst if x>0), sum(filter(lambda x: x<0, lst))] if len(lst)>0 else []

