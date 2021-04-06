
def operation(a, b, op):
  operations = {
    'add': lambda x, y: int(x) + int(y),
    'subtract': lambda x, y: int(x) - int(y),
    'divide': lambda x, y: int(int(x) / int(y)),
    'multiply': lambda x, y: int(x) * int(y)
  }
  try:
    return str(operations[op](a, b))
  except:
    return 'undefined'

