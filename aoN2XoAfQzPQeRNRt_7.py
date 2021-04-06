
op_dict = {
  'add' : '+',
  'subtract' : '-',
  'multiply' : '*',
  'divide' : '/'
}
def operation(a, b, op):
  try:
    expr = a + op_dict[op] + b
    res = round(eval(expr))
    return str(res)
  except ZeroDivisionError:
    return 'undefined'

