
def operation(a, b, op):
  x = {"add": '+','subtract': '-', 'divide': '/', 'multiply': '*'}[op]
  try:
    return str(int(eval(a+x+b)))
  except:
    return 'undefined'

