
def convert(deg):
  x = deg.replace('C', '').replace('F', '').replace('*', '')
  if 'C' in deg:
    t = round(int(x) * 9 / 5 + 32)
    return str(t) + '*F'
  elif 'F' in deg:
    t = round(5 / 9 * (int(x) - 32))
    return str(t) + '*C'
  else:
    return 'Error'

