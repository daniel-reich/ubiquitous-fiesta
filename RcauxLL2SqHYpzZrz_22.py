
def true_equations(lst):
  return [x for x in lst if eval(x.replace('=', '==')) == True]

