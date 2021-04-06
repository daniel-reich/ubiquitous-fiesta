
def math_expr(expr):
  key = "1234567890+-*/%= "
  new_string = ""
  for ch in expr:
    if ch in key:
      new_string += ch
  if new_string == expr:
    return True
  else:
    return False

