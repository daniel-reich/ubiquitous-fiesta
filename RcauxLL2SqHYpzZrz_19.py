
def true_equations(lst):
 return [equation for equation in lst if eval(equation.replace("=","=="))]

