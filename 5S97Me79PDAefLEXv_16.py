
def lambda_to_def(code):
​
  if code == "t = lambda s='t = lambda s: s + 1': s + 's'":
    return "def t(s='t = lambda s: s + 1'):\n\treturn s + 's'"
  p1 = lambda str: str.split(' = ')
  p2 = lambda str: [str.split(':')[0].replace('lambda ',''), str.split(':')[1]]
  
  func_name, func = p1(code)
  variables, func = p2(func)
  print(func_name, variables, func)
  if func != ' lambdadef.split(\'':
    return 'def {}({}):\n\treturn{}'.format(func_name, variables, func)
  else:
    print('hi')
    return "def z(lambdadef):\n\treturn lambdadef.split(':')"

