
def eval_algebra(eq):
  
  eq = eq.split('=')
​
  if eq[0] == 'x':
    return eval(eq[1])
  elif eq[1] == 'x':
    return eval(eq[1])
  else:
​
    for x in range(-1000, 1000):
      t = eval(eq[0] + '==' + eq[1])
      if t == True:
        return x

