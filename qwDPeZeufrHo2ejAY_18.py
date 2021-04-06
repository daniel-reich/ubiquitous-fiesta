
def eval_algebra(eq):
  lhs_rhs = eq.split("=")
  if "x" in lhs_rhs[1]:
    return eval(lhs_rhs[0])
  elelents = lhs_rhs[0][:-1].split(" ")
  if "x" in elelents[0]:
    return eval(lhs_rhs[1] + elelents[1] + "-" + elelents[2])
  return eval(elelents[1] + "(" + lhs_rhs[1] + "-" + elelents[0] + ")")

