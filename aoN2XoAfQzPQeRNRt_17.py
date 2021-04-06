
def operation(a, b, op) :
  #return "a op b"
  operators = {"add": "+", "subtract":"-", "divide":"//", "multiply":"*"}
  try: return str(eval(a + operators[op] + b)) 
  except: return "undefined"

