
def product(lst):
  ordered_lst  = sorted(set(lst));
  print(ordered_lst);
  return ordered_lst[-1] * ordered_lst[-2] if (len(ordered_lst) > 1) else ordered_lst[-1]**2 ;

