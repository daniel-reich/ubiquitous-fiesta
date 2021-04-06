
def convert(deg):
  if deg[-1] == 'C':
    return str(round(int(deg[:deg.index('*')]) * 9 / 5 + 32)) + '*F'
  elif deg[-1] == 'F':
    return str(round((int(deg[:deg.index('*')]) - 32) * 5/9)) + '*C'
  else:
    return 'Error'

