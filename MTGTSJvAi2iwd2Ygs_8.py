
def valid_division(d):
  try:
    return eval(d) == eval(d.replace('/', '//'))
  except ZeroDivisionError:
    return "invalid"

