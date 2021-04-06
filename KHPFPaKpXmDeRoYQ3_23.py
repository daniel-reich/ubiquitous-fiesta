
def check_score(s):
  h = 5
  O = 3
  X = 1
  E = -1
  C = -3
  L = -5
  
  s = [i for l in s for i in l]
  expr = []
  
  for item in s:
    if item in 'OX':
      expr.append(item)
    elif item == '#':
      expr.append('h')
    elif item == '!':
      expr.append('E')
    elif item == '!!':
      expr.append('C')
    elif item == '!!!':
      expr.append('L')
  print(','.join(expr) + '\n' + str(s))
  return eval('+'.join(expr)) if eval('+'.join(expr))>=0 else 0

