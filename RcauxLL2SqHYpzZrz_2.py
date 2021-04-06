
def true_equations(lst):
  return [eq for eq in lst if eval(eq.split("=")[0])==int(eq.split("=")[-1])]

