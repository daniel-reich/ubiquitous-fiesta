
def sum_fractions(lst):
  float_lst = [e[0]/e[1] for e in lst]
  return int(sum(float_lst))

