
def convert(deg):
  if '*F' in deg:
    return str(round((int(deg[:-2]) - 32) * 5/9)) + '*C'
  if '*C' in deg:
    return str(round(int(deg[:-2]) * 9/5 + 32)) + '*F'
  return 'Error'

