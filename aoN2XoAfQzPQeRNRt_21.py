
def operation(a, b, op):
  if b=="0" and op=='divide':
    return 'undefined'
  return str(eval(a+{'add':'+','subtract':'-','divide':'//','multiply':'*'}[op]+b))

