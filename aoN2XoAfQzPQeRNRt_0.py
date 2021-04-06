
def operation(a, b, op):
  operations={"add":"+","subtract":"-","divide":"/","multiply":"*"}
  return "undefined" if op=="divide" and b=="0" else str(round(eval(a+operations[op]+b)))

