
def true_equations(lst):
  return [i for i in lst if eval(i.split('=')[0])==eval(i.split('=')[1])]

