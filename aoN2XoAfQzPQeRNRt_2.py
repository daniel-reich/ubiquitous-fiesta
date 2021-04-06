
def operation(a,b,o):
  try:return str(round(eval(a+{'a':'+','s':'-','d':'/','m':'*'}[o[0]]+b)))
  except:return'undefined'

