
def solve(eq):
  if "+" in eq:
    num1, num2 = eq.split("+")[1].split("=")
    return eval(num2 + "-" + num1)
  else:
    num1, num2 = eq.split("-")[1].split("=")
    return eval(num2 + "+" + num1)

