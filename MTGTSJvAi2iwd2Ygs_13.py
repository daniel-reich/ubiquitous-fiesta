
def valid_division(d):
  try:
    d = d.split('/')
    return int(d[0]) % int(d[1]) == 0
  except ZeroDivisionError:
    return 'invalid'

