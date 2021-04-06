
def true_equations(lst):
  return [x for x in lst if eval(x.split('=')[0]) == eval(x.split('=')[1])]

