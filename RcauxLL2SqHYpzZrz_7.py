
def true_equations(lst):
  return [e for e in lst if check_eq(e)];
​
def check_eq(eq):
  left , right = eq.split("=");
  return eval(left) == eval(right);

