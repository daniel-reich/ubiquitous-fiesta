
def true_equations(lst):
  return [eq for eq in lst if eval(eq.replace("=", "=="))]

