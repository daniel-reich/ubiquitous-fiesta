
def operation(a, b, op):
  dictionary ={
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "divide": "/"
  }
  try:
    return str(int(eval(a+dictionary[op]+b)))
  except ZeroDivisionError:
    return "undefined"

