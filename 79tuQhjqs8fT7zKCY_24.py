
def postfix(expr):
  expr = expr.split()
  stk = []
  for el in expr:
    if el in ('+-*/'):
      b = stk.pop()
      a = stk.pop()
      stk.append(str(eval(a + el + b)))
    else:
      stk.append(el)
  return int(float(stk.pop()))

