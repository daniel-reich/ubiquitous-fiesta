
def operation(a, b, op):
  d = {"add": "+", "subtract": "-", "multiply": "*", "divide": "//"}
  try:
    return str(eval(a + d[op] + b))
  except:
    return "undefined"

