
def operation(a, b, op):
  if op == "divide" and b == "0":
    return "undefined"
  
  o = {"add": "+", "subtract": "-", "multiply": "*", "divide": "//"}[op]
  return str(eval("(%s)%s(%s)" % (a, o, b)))

