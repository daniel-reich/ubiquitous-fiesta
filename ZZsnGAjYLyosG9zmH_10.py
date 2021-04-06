
def flash(f):
  try:
    if f[1] == '+':
      return f[0] + f[2]
    if f[1] == '-':
      return f[0] - f[2]
    if f[1] == 'x':
      return f[0] * f[2]
    if f[1] == '/':
      return round(f[0] / f[2], 2)
  except ZeroDivisionError:
    return None

