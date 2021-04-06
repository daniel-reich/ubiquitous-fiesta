
def true_equations(lst):
  return [exp for exp in lst if eval(exp.replace('=','=='))]

