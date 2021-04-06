
from operator import add, sub, mul, floordiv
def arithmetic_operation(n):
  operators = {"+": add, "-": sub, "*": mul, "//": floordiv}
  tokens, token = list(), str()
  for c in n+" ":
    if c == " ": 
      tokens.append(token)
      token = str()
    else: token += c
  if tokens[1] == "//" and tokens[-1] == "0": return -1
  else:
    a, b = int(tokens[0]), int(tokens[-1])
    return operators[tokens[1]](a, b)

