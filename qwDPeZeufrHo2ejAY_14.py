
def eval_algebra(eq):
  eq = eq.split(" = ")
  if not "x" in eq[0]:
    return eval(eq[0])
  elif eq[0][0] == "x" or "+" in eq[0]:
    eq[0] = eq[0].replace("x",str("-") + eq[1]) 
    return -1 * eval(eq[0])
  else:
    eq[0] = eq[0].replace("x", eq[1])
    return eval(eq[0])

