
def sum_neg(lst):
  return [len([i for i in lst if i>0]),sum(i for i in lst if i<0)] if len(lst)>0 else []

