
def postfix(expr):
  items = expr.split(" ")
  i = len(items)-1
​
  def recurse():
    nonlocal i
    op = items[i]
    i -= 1
    if "0" <= op <= "9":
      return int(op)
    if op == "+":
      return recurse()+recurse()
    if op == "-":  # next read item is second operand
      return -recurse()+recurse()
    if op == "*":
      return recurse()*recurse()
    if op == "/":  # ^
      return 1/recurse()*recurse()
    raise Exception("unsupported action: "+op)
​
  return recurse()

