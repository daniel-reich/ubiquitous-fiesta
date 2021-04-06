
def every_some(test, val, a, b, c, d, e):
  if val == 'everybody':
    for i in [a,b,c,d,e]:
      exp = str(i) + test
      if not eval(exp):
        return False
    return True
  else:
    for i in [a,b,c,d,e]:
      exp = str(i) + test
      if eval(exp):
        return True
    return False

