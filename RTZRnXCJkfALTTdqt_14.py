
def sum_neg(lst):
  return [] if len(lst)==0 else [len([i for i in lst if int(i)>0]),sum([i for i in lst if int(i)<0])]

