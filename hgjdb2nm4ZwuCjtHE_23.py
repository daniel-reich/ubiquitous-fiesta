
def math_expr(expr):
  signs = "+-*/%"
  lst = [i for i in expr. replace(" ", "")]
  if len(lst) != 3:
    return False
  return lst[0].isnumeric() and lst[1] in signs and lst[2].isnumeric()

