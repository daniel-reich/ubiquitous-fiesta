
def convert(deg):
  try:
    num = int(deg[:-2])
    if deg[-1] == 'C':
      return "{}*F".format(round(num * 9/5) + 32, 0)
    return "{}*C".format(round((num - 32) * 5/9), 0)
  except:
    return 'Error'

