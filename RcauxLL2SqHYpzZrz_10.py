
def true_equations(lst):
  return [e for e in lst if eval(e.split('=')[0])==eval(e.split('=')[1])]

