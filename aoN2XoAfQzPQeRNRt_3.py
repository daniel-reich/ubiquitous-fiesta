
def operation(a, b, op):
  operator = {"add" : "+", "subtract" : "-", 
        "divide" : "//", "multiply" : "*"}
  try:
    return str(eval(a + operator[op] + b))
  except:
    return "undefined"

