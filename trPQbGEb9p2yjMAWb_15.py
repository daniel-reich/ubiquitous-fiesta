
def every_some(test, val, *variables):
  if val == 'everybody':
    return all(eval(str(x) + test) for x in variables)
  else:
    return any(eval(str(x) + test) for x in variables)

