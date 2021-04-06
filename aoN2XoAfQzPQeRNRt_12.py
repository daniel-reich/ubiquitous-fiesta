
def operation(a, b, op):
  operations = {'add':'+', 'subtract':'-', 'multiply':'*', 'divide':'//'}
  try:
    return str(eval(a + operations[op] + b))
  except:
    return 'undefined'

