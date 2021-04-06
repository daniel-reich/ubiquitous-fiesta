
def lambda_to_def(code):
  n1, n2 = code.index('='), code.rindex(': ')
  name = code[:n1-1]
  var = code[n1+9:n2]
  func = code[n2+2:]
  return 'def {}({}):\n\treturn {}'.format(name, var, func)

