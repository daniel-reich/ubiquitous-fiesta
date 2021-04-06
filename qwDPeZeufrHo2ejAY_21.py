
def eval_algebra(eq):
  eq = eq.split(" ")
  if eq[0] == "x":
    return int(eq[4]) - (int(eq[1]+eq[2]))
  if eq[2] == "x":
    return eval(eq[1] + "(" + eq[4] + "-" + eq[0] + ")")
  if eq[4] == "x":
    return eval(eq[0]+eq[1]+eq[2])

