
def every_some(test, val, *variables):
  #variables = [a,b,c,d,e]
  res = []
  for v in variables:
    res.append(eval(str(v)+test))
    
  res = sum(res)
  if val == 'everybody':
    return res == len(variables)
  else:
    return res >= 1

